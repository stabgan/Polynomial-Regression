# Polynomial Regression

Comparing linear vs. polynomial regression on a salary dataset — implemented in both Python and R.

## Overview

This project fits a degree-4 polynomial regression model to a small dataset of job positions and salaries (10 data points). It compares the fit against a simple linear regression to demonstrate how polynomial features capture non-linear relationships.

The dataset (`Position_Salaries.csv`) maps job levels 1–10 to salaries ranging from 45k to 1M, which follow an exponential-like curve — a good candidate for polynomial fitting.

### Mathematical Model

```
y = b₀ + b₁x + b₂x² + b₃x³ + b₄x⁴
```

## Approach

1. Load the position/salary dataset
2. Fit a simple linear regression as a baseline
3. Fit a degree-4 polynomial regression
4. Visualize both fits against the actual data (including a high-resolution smooth curve)
5. Predict salary for a new position level (6.5)

## Files

| File | Description |
|------|-------------|
| `polynomial_regression.py` | Python implementation using scikit-learn and matplotlib |
| `polynomial_regression.R` | R implementation using base `lm()` and ggplot2 |
| `Position_Salaries.csv` | Dataset: 10 positions with level and salary columns |

## Dependencies

### Python

- Python 3.x
- numpy
- pandas
- matplotlib
- scikit-learn

```bash
pip install numpy pandas matplotlib scikit-learn
```

### R

- R 3.x+
- ggplot2

```r
install.packages("ggplot2")
```

## Usage

```bash
# Python
python polynomial_regression.py

# R
Rscript polynomial_regression.R
```

Both scripts display three plots (linear fit, polynomial fit, smooth polynomial curve) and print a salary prediction for level 6.5.

## Known Issues

- **Deprecated API (Python):** `lin_reg.predict(6.5)` and `lin_reg_2.predict(poly_reg.fit_transform(6.5))` pass scalars directly. Modern scikit-learn requires 2D array input, e.g. `lin_reg.predict([[6.5]])`. These calls will raise a `ValueError` on current versions of scikit-learn.
- **Deprecated import (Python):** A commented-out line references `sklearn.cross_validation`, which was removed in scikit-learn 0.20. The correct module is `sklearn.model_selection`.
- **No train/test split:** Both implementations train and evaluate on the full dataset (the split code is commented out). This is fine for demonstration but means there's no out-of-sample validation.
- **Hardcoded file path:** Both scripts assume `Position_Salaries.csv` is in the current working directory.

## License

MIT
