
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed_deforestation.csv"
RESULTS_DIR = BASE_DIR / "results"

RESULTS_DIR.mkdir(exist_ok=True)

# Load processed dataset
df = pd.read_csv(DATA_PATH)
df = df.sort_values("Year")

print("Dataset loaded successfully!")
print(df.head())

# Define input and target
X = df[["Year"]]
y = df["Forest_Area"]

# Chronological train-test split (80:20)
split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 4))

# Predict future forest area
future_years = pd.DataFrame({
    "Year": np.arange(2026, 2031)
})

future_predictions = model.predict(future_years)

future_years["Predicted_Forest_Area"] = future_predictions

print("\nFuture Forest Area Predictions:")
print(future_years)

# Save predictions
future_years.to_csv(
    RESULTS_DIR / "future_predictions.csv",
    index=False
)

# Save evaluation metrics
with open(RESULTS_DIR / "model_metrics.txt", "w") as f:
    f.write(f"Mean Absolute Error: {mae:.2f}\n")
    f.write(f"R2 Score: {r2:.4f}\n")

# Plot results
plt.figure(figsize=(10, 6))

plt.plot(
    df["Year"],
    df["Forest_Area"],
    marker="o",
    label="Historical Forest Area"
)

plt.plot(
    future_years["Year"],
    future_years["Predicted_Forest_Area"],
    marker="x",
    linestyle="--",
    label="Predicted Forest Area"
)

plt.xlabel("Year")
plt.ylabel("Forest Area (Synthetic Units)")
plt.title("Deforestation Analysis and Prediction")
plt.legend()
plt.grid(True)

plt.savefig(
    RESULTS_DIR / "deforestation_prediction.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nModel training completed successfully!")
print("Results saved in the results folder.")
