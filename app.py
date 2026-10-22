
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "processed_deforestation.csv"
PREDICTION_PATH = BASE_DIR / "results" / "future_predictions.csv"

# Page configuration
st.set_page_config(
    page_title="Deforestation Analysis",
    page_icon="🌳",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
.main-title {
    font-size: 38px;
    font-weight: bold;
    color: #228B22;
    text-align: center;
}
.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🌳 Deforestation Analysis Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Machine Learning Based Forest Cover Prediction</div>',
    unsafe_allow_html=True
)

st.warning(
    "Educational prototype using synthetic data. "
    "Predictions are not real-world forest-cover forecasts."
)

st.divider()

# Load datasets
if not DATA_PATH.exists() or not PREDICTION_PATH.exists():
    st.error(
        "Required datasets are missing. Run "
        "src/preprocessing.py and src/prediction.py first."
    )
    st.stop()

df = pd.read_csv(DATA_PATH)
predictions = pd.read_csv(PREDICTION_PATH)

# Sidebar
st.sidebar.title("🌲 Dashboard Controls")
st.sidebar.write("Research Methodology - Experiment 7")

selected_year = st.sidebar.slider(
    "Select Year",
    min_value=int(df["Year"].min()),
    max_value=int(df["Year"].max()),
    value=int(df["Year"].max())
)

selected_data = df[df["Year"] == selected_year]

# Metrics
st.subheader("📊 Forest Cover Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Forest Area",
        f"{selected_data['Forest_Area'].iloc[0]:,.0f}"
    )

with col2:
    st.metric(
        "Deforestation Rate",
        f"{selected_data['Deforestation_Rate'].iloc[0]:.2f}%"
    )

with col3:
    total_loss = (
        df["Forest_Area"].iloc[0]
        - selected_data["Forest_Area"].iloc[0]
    )
    st.metric("Total Forest Loss", f"{total_loss:,.0f}")

st.divider()

# Historical forest cover
st.subheader("🌳 Historical Forest Cover")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(
    df["Year"],
    df["Forest_Area"],
    color="forestgreen",
    marker="o",
    linewidth=2
)
ax.set_xlabel("Year")
ax.set_ylabel("Forest Area (Synthetic Units)")
ax.set_title("Historical Forest Cover Trend")
ax.grid(True, alpha=0.3)
st.pyplot(fig)
plt.close(fig)

# Deforestation rate
st.subheader("📉 Annual Deforestation Rate")

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.bar(
    df["Year"],
    df["Deforestation_Rate"],
    color="orange"
)
ax2.set_xlabel("Year")
ax2.set_ylabel("Deforestation Rate (%)")
ax2.set_title("Annual Deforestation Rate")
st.pyplot(fig2)
plt.close(fig2)

# Future predictions
st.subheader("🔮 Future Forest Cover Predictions")

st.dataframe(
    predictions,
    use_container_width=True,
    hide_index=True
)

fig3, ax3 = plt.subplots(figsize=(10, 5))

ax3.plot(
    df["Year"],
    df["Forest_Area"],
    label="Historical Data",
    color="green",
    marker="o"
)

ax3.plot(
    predictions["Year"],
    predictions["Predicted_Forest_Area"],
    label="Predicted Data",
    color="red",
    linestyle="--",
    marker="x"
)

ax3.set_xlabel("Year")
ax3.set_ylabel("Forest Area (Synthetic Units)")
ax3.set_title("Forest Cover Prediction")
ax3.legend()
ax3.grid(True, alpha=0.3)

st.pyplot(fig3)
plt.close(fig3)

st.divider()

# Dataset preview
st.subheader("📁 Dataset Preview")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# Download predictions
st.download_button(
    label="📥 Download Prediction Results",
    data=predictions.to_csv(index=False),
    file_name="deforestation_predictions.csv",
    mime="text/csv"
)
# Calculate total forest loss percentage
initial_forest = df["Forest_Area"].iloc[0]
current_forest = selected_data["Forest_Area"].iloc[0]

loss_percentage = (
    (initial_forest - current_forest) / initial_forest
) * 100

st.metric(
    "Total Forest Loss Percentage",
    f"{loss_percentage:.2f}%"
)
st.divider()

st.caption(
    "Research Methodology Lab | Experiment 7 | "
    "Deforestation Analysis and Prediction | Version 1.3"
)
