# Polynomial Regression

Comparing linear vs. polynomial regression on a salary dataset — implemented in both Python and R.

## Overview

This project fits a degree-4 polynomial regression model to a small dataset of job positions and salaries (10 data points). It compares the fit against a simple linear regression to demonstrate how polynomial features capture non-linear relationships.

The dataset (`Position_Salaries.csv`) maps job levels 1-10 to salaries ranging from 45k to 1M, which follow an exponential-like curve, a good candidate for polynomial fitting.

### Mathematical Model

```
y = b0 + b1*x + b2*x^2 + b3*x^3 + b4*x^4
```

## Methodology

1. Load the position/salary dataset
2. Fit a simple linear regression as a baseline
3. Generate polynomial features (degree 4) and fit a polynomial regression
4. Visualize both fits against the actual data, including a high-resolution smooth curve
5. Predict salary for a new position level (6.5)

## Dataset

`Position_Salaries.csv` contains 10 rows mapping job titles and levels to salaries. Only the `Level` and `Salary` columns are used as features and target.

## Files

| File | Description |
|------|-------------|
| `polynomial_regression.py` | Python implementation using scikit-learn and matplotlib |
| `polynomial_regression.R` | R implementation using base `lm()` and ggplot2 |
| `Position_Salaries.csv` | Dataset: 10 positions with level and salary columns |

## Tech Stack

| | Technology | Purpose |
|---|---|---|
| :snake: | Python 3.x | Primary implementation |
| :bar_chart: | scikit-learn | Linear and polynomial regression |
| :chart_with_upwards_trend: | matplotlib | Plotting |
| :panda_face: | pandas / numpy | Data loading and manipulation |
| :chart_with_downwards_trend: | R 3.x+ | Alternative implementation |
| :art: | ggplot2 | R visualization |

## Dependencies

### Python

```bash
pip install numpy pandas matplotlib scikit-learn
```

### R

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

- **No train/test split:** Both implementations train and evaluate on the full dataset (split code is commented out). Fine for demonstration, but there is no out-of-sample validation.
- **Small dataset:** Only 10 data points. A degree-4 polynomial on this data is for illustration, not production use.

## License

MIT
