
import pandas as pd
from pathlib import Path

# Define project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "deforestation.csv"
OUTPUT_PATH = BASE_DIR / "data" / "processed_deforestation.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

print("Original Dataset:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Handle missing values
df = df.dropna(subset=["Year", "Forest_Area"])

# Convert columns to numeric
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Forest_Area"] = pd.to_numeric(
    df["Forest_Area"], errors="coerce"
)

# Remove invalid rows
df = df.dropna(subset=["Year", "Forest_Area"])
df = df[df["Forest_Area"] >= 0]

# Sort by year
df = df.sort_values(by="Year").reset_index(drop=True)

# Calculate annual deforestation rate
df["Deforestation_Rate"] = (
    (df["Forest_Area"].shift(1) - df["Forest_Area"])
    / df["Forest_Area"].shift(1)
) * 100

df["Deforestation_Rate"] = df["Deforestation_Rate"].fillna(0)

# Save processed dataset
df.to_csv(OUTPUT_PATH, index=False)

print("\nProcessed Dataset:")
print(df.head())

print("\nData preprocessing completed successfully!")
print("Processed dataset saved to:", OUTPUT_PATH)
