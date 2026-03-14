# Polynomial Regression
# Comparing linear vs. polynomial regression on a salary dataset.

# Importing the libraries
import os
import sys

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def load_dataset():
    """Load the Position_Salaries dataset relative to this script's location."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "Position_Salaries.csv")

    if not os.path.isfile(csv_path):
        print(f"Error: dataset not found at {csv_path}", file=sys.stderr)
        sys.exit(1)

    dataset = pd.read_csv(csv_path)
    X = dataset.iloc[:, 1:2].values  # Level (2D array)
    y = dataset.iloc[:, 2].values    # Salary
    return X, y


def fit_models(X, y, degree=4):
    """Fit a linear regression and a polynomial regression of the given degree."""
    # Linear regression
    lin_reg = LinearRegression()
    lin_reg.fit(X, y)

    # Polynomial regression
    poly_features = PolynomialFeatures(degree=degree)
    X_poly = poly_features.fit_transform(X)
    poly_reg = LinearRegression()
    poly_reg.fit(X_poly, y)

    return lin_reg, poly_reg, poly_features


def plot_results(X, y, lin_reg, poly_reg, poly_features):
    """Visualise linear vs. polynomial regression fits."""
    # Linear regression plot
    plt.figure()
    plt.scatter(X, y, color="red")
    plt.plot(X, lin_reg.predict(X), color="blue")
    plt.title("Truth or Bluff (Linear Regression)")
    plt.xlabel("Position Level")
    plt.ylabel("Salary")
    plt.tight_layout()
    plt.show()

    # Polynomial regression plot
    plt.figure()
    plt.scatter(X, y, color="red")
    plt.plot(X, poly_reg.predict(poly_features.fit_transform(X)), color="blue")
    plt.title("Truth or Bluff (Polynomial Regression)")
    plt.xlabel("Position Level")
    plt.ylabel("Salary")
    plt.tight_layout()
    plt.show()

    # Smooth polynomial curve (higher resolution)
    X_grid = np.arange(float(X.min()), float(X.max()), 0.1).reshape(-1, 1)
    plt.figure()
    plt.scatter(X, y, color="red")
    plt.plot(X_grid, poly_reg.predict(poly_features.transform(X_grid)), color="blue")
    plt.title("Truth or Bluff (Polynomial Regression — Smooth)")
    plt.xlabel("Position Level")
    plt.ylabel("Salary")
    plt.tight_layout()
    plt.show()


def predict_salary(level, lin_reg, poly_reg, poly_features):
    """Predict salary for a given position level using both models."""
    level_2d = np.array([[level]])

    linear_pred = lin_reg.predict(level_2d)[0]
    poly_pred = poly_reg.predict(poly_features.transform(level_2d))[0]

    print(f"\nPredictions for level {level}:")
    print(f"  Linear Regression:     ${linear_pred:,.0f}")
    print(f"  Polynomial Regression: ${poly_pred:,.0f}")

    return linear_pred, poly_pred


def main():
    X, y = load_dataset()
    lin_reg, poly_reg, poly_features = fit_models(X, y, degree=4)
    plot_results(X, y, lin_reg, poly_reg, poly_features)
    predict_salary(6.5, lin_reg, poly_reg, poly_features)


if __name__ == "__main__":
    main()
