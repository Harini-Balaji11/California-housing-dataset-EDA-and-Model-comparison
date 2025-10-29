
## California Housing Dataset — EDA and Model Comparison

This repository contains an end‑to‑end exploratory data analysis (EDA) and baseline model comparison on the California Housing dataset from `scikit‑learn`. It is designed to be portfolio‑ready, easy to run, and professional for reviewers.

### Highlights
- **Clean EDA**: Distribution, correlations, geospatial context, outliers
- **Baselines**: Linear Regression, Ridge, Lasso, Random Forest, Gradient Boosting
- **Reproducible**: One‑command setup and HTML report export
- **Well‑structured**: Clear directories, scripts, and environment setup

### Repository Structure
```
.
├─ notebooks/
│  └─ 01_eda_california_housing.ipynb        # Main EDA & insights
├─ scripts/
│  ├─ run_eda.py                             # Generate EDA figures
│  └─ run_models.py                          # Train & compare models
├─ reports/
│  ├─ figures/                               # Auto‑generated plots
│  └─ eda_report.html                        # Optional HTML export
├─ requirements.txt
├─ Makefile                                  # Export notebook to HTML
├─ .gitignore
├─ LICENSE
└─ README.md
```

### Quickstart
1) Create and activate a virtual environment (recommended)
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

2) Install dependencies
```bash
pip install -r requirements.txt
```

3) Run EDA figures and baseline model comparison
```bash
python scripts/run_eda.py
python scripts/run_models.py
```

4) Optional: Export notebook as an HTML report
```bash
make report
```
The figures are saved in `reports/figures/` and the HTML report to `reports/eda_report.html`.

### Dataset
The California Housing dataset is loaded via `sklearn.datasets.fetch_california_housing`. No external download is needed. Target is `MedHouseVal`; features include `MedInc`, `HouseAge`, `AveRooms`, `AveBedrms`, `Population`, `AveOccup`, `Latitude`, and `Longitude`.

### What’s inside the notebook
- Data overview and sanity checks (shape, types, missing values)
- Descriptive statistics and target analysis (skew, outliers)
- Feature distributions and correlation heatmap
- Simple geospatial scatter by latitude/longitude
- Baseline regressors and evaluation (e.g., MAE, RMSE, R²)

### Reproducing results
All results can be reproduced by running the scripts and/or opening `notebooks/01_eda_california_housing.ipynb`. To create a shareable report, use `make report` which converts the notebook to HTML via `nbconvert`.

### Requirements
See `requirements.txt` for pinned packages. Key libraries:
- pandas, numpy, matplotlib, seaborn
- scikit‑learn
- jupyter, nbconvert

### License
This project is released under the MIT License. See `LICENSE` for details.

### Acknowledgments
Dataset provided by `scikit‑learn`. Inspiration: common EDA and baseline modeling workflows for tabular regression problems.