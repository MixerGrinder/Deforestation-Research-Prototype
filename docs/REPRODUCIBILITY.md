
# Reproducibility Report

## Project
Deforestation Analysis and Prediction Using Machine Learning

## Experiment
Research Methodology Lab - Experiment 7

## Objective
To verify that the research prototype can be
executed repeatedly and produces consistent results.

## Environment
- Operating System: Windows
- Python: 3.12.10
- Dependencies: requirements.txt
- IDE: Visual Studio Code

## Dataset
The prototype uses a synthetic forest-cover dataset
covering the years 2010 to 2025.

File: data/deforestation.csv

## Execution Procedure

1. Create and activate a Python virtual environment.
2. Install dependencies from requirements.txt.
3. Run data preprocessing.
4. Train the Linear Regression model.
5. Generate future predictions.
6. Execute automated tests.
7. Launch the Streamlit dashboard.

## Commands

python -m pip install -r requirements.txt

python src/preprocessing.py

python src/prediction.py

python -m unittest discover -s tests -v

python -m streamlit run app.py

## Verification Criteria

- Preprocessing completes without errors.
- Prediction results are generated.
- Evaluation metrics are saved.
- All six automated tests pass.
- The Streamlit dashboard opens successfully.
- Repeated executions produce consistent results.

## Limitations

The dataset is synthetic and is intended for
educational demonstration.

Reproducibility of the software does not establish
real-world predictive accuracy.

## Verification Status

Pending final execution and confirmation.
