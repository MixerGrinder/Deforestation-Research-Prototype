
# Deforestation Analysis and Prediction Using Machine Learning

## Research Methodology Lab – Experiment 7

**Academic Year:** 2026–27  
**Semester:** V  
**Department:** CSE – Data Science  
**Institution:** A. P. Shah Institute of Technology, Thane

## 1. Project Title

Deforestation Analysis and Prediction Using Machine Learning

## 2. Problem Statement

Deforestation is a major environmental concern that contributes
to biodiversity loss, climate change, soil erosion, and
ecological imbalance.

This project develops a machine learning prototype to analyze
historical forest-cover data, identify deforestation trends,
and estimate future forest-cover changes.

## 3. Objectives

- Analyze historical forest-cover data.
- Perform data cleaning and preprocessing.
- Identify trends in deforestation.
- Train a machine learning prediction model.
- Visualize forest-cover changes.
- Develop an interactive dashboard.
- Maintain project versions using Git and GitHub.
- Ensure reproducibility through documentation and testing.

## 4. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Git and GitHub
- Visual Studio Code

## 5. System Requirements

### Hardware
- Computer or laptop
- Minimum 4 GB RAM
- Internet connection for initial setup

### Software
- Windows 10/11 or compatible operating system
- Python 3.12
- Git
- VS Code
- Required Python libraries

## 6. System Architecture

Input Dataset
     |
     v
Data Preprocessing
     |
     v
Processed Dataset
     |
     v
Linear Regression Model
     |
     v
Forest-Cover Prediction
     |
     v
Results and Visualization
     |
     v
Streamlit Dashboard

## 7. Methodology

### Step 1: Data Collection

A synthetic forest-cover dataset is used to demonstrate
the prototype. It contains annual observations from
2010 to 2025.

The dataset is illustrative and does not represent
measurements from a specific geographic region.

### Step 2: Data Preprocessing

The preprocessing module:
- Loads the dataset.
- Checks missing values.
- Removes duplicate records.
- Removes invalid observations.
- Sorts data chronologically.
- Calculates annual deforestation rates.

### Step 3: Machine Learning

Linear Regression is used to model the relationship
between year and forest-cover area.

Input Feature: Year

Target Variable: Forest_Area

### Step 4: Prediction

The trained model estimates forest-cover area
for the years 2026–2030.

### Step 5: Visualization

Matplotlib generates graphs showing historical
forest-cover trends and future predictions.

### Step 6: Dashboard

Streamlit provides an interactive interface with:
- Forest-cover statistics
- Annual deforestation rates
- Historical trend graphs
- Future prediction results
- Dataset preview
- CSV download functionality

## 8. Installation Instructions

Clone the GitHub repository:

git clone https://github.com/MixerGrinder/Deforestation-Research-Prototype

Navigate to the project:

cd Deforestation-Research-Prototype

Create a virtual environment:

py -3.12 -m venv .venv

Activate the environment:

.\.venv\Scripts\Activate.ps1

Install dependencies:

python -m pip install -r requirements.txt

## 9. Execution Instructions

Run data preprocessing:

python src/preprocessing.py

Train the prediction model:

python src/prediction.py

Launch the dashboard:

python -m streamlit run app.py

Open the local URL:

http://localhost:8501

## 10. Input and Output

### Input

data/deforestation.csv

Dataset columns:
- Year
- Forest_Area
- Deforestation_Rate

### Output

data/processed_deforestation.csv

results/future_predictions.csv

results/model_metrics.txt

results/deforestation_prediction.png

## 11. Model Evaluation

The prediction model is evaluated using:

- Mean Absolute Error (MAE)
- R-squared Score (R2)

The evaluation values are generated during model execution
and saved in results/model_metrics.txt.

## 12. Version Control

Git and GitHub are used to maintain the project history.

Development stages:
- V1.0: Initial prototype
- V1.1: Data preprocessing
- V1.2: Machine learning model
- V1.3: Streamlit dashboard
- V2.0: Final tested and documented prototype

Note: Version labels describe development stages.
Actual Git tags and commits must be verified in the repository.

## 13. Testing

Automated tests verify:
- Dataset availability and structure
- Missing values
- Valid forest-cover values
- Chronological ordering
- Basic machine learning model training

Run tests using:

python -m unittest discover -s tests -v

## 14. Results

The prototype demonstrates:
- Forest-cover data preprocessing
- Linear Regression model training
- Prediction generation for 2026–2030
- Visualization of forest-cover trends
- Interactive dashboard functionality

The current dataset is synthetic, so predictions are
for educational demonstration only.

## 15. Limitations

- Uses a small synthetic dataset.
- Does not include satellite imagery.
- Uses only year as the prediction feature.
- Assumes an approximately linear trend.
- Does not account for environmental or policy changes.
- Cannot provide validated real-world forecasts.

## 16. Future Scope

- Integrate real satellite and forest-cover datasets.
- Apply Random Forest and other ML algorithms.
- Add region-wise deforestation analysis.
- Integrate GIS maps.
- Improve prediction accuracy with additional features.
- Deploy the dashboard online.

## 17. Reproducibility

The project includes:
- Source code
- Dataset
- requirements.txt
- Installation instructions
- Execution instructions
- Automated tests
- Git version history

Another user can clone the repository, install dependencies,
run preprocessing, train the model, and launch the dashboard.

## 18. References

- Python Documentation: https://docs.python.org/3/
- Pandas Documentation: https://pandas.pydata.org/docs/
- Scikit-learn Documentation: https://scikit-learn.org/
- Streamlit Documentation: https://docs.streamlit.io/
- Git Documentation: https://git-scm.com/doc
