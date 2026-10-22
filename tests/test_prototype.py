
import unittest
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed_deforestation.csv"


class TestDeforestationPrototype(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv(DATA_PATH)

    def test_dataset_not_empty(self):
        self.assertFalse(self.df.empty)

    def test_required_columns(self):
        required = [
            "Year",
            "Forest_Area",
            "Deforestation_Rate"
        ]
        for column in required:
            self.assertIn(column, self.df.columns)

    def test_missing_values(self):
        self.assertFalse(
            self.df.isnull().values.any()
        )

    def test_forest_area_positive(self):
        self.assertTrue(
            (self.df["Forest_Area"] >= 0).all()
        )

    def test_years_sorted(self):
        self.assertTrue(
            self.df["Year"].is_monotonic_increasing
        )

    def test_model_training(self):
        X = self.df[["Year"]]
        y = self.df["Forest_Area"]

        model = LinearRegression()
        model.fit(X, y)

        prediction = model.predict(
            pd.DataFrame({"Year": [2026]})
        )

        self.assertEqual(len(prediction), 1)


if __name__ == "__main__":
    unittest.main()
