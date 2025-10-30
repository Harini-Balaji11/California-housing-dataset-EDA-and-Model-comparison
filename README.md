
## California Housing Dataset — EDA and Model Comparison

[![CI](https://github.com/Harini-Balaji11/California-housing-dataset-EDA-and-Model-comparison/actions/workflows/ci.yml/badge.svg)](https://github.com/Harini-Balaji11/California-housing-dataset-EDA-and-Model-comparison/actions/workflows/ci.yml)
[![Pages](https://github.com/Harini-Balaji11/California-housing-dataset-EDA-and-Model-comparison/actions/workflows/pages.yml/badge.svg)](https://github.com/Harini-Balaji11/California-housing-dataset-EDA-and-Model-comparison/actions/workflows/pages.yml)

Live report: https://Harini-Balaji11.github.io/California-housing-dataset-EDA-and-Model-comparison/

This repository contains an end‑to‑end exploratory data analysis (EDA) and baseline model comparison on the California Housing dataset from `scikit‑learn`. It is designed to be portfolio‑ready, easy to run, and professional for reviewers.

### Highlights
- **Clean EDA**: Distribution, correlations, geospatial context, outliers
- **Baselines**: Linear Regression, Ridge, Lasso, Random Forest, Gradient Boosting
- **Reproducible**: One‑command setup and HTML report export
- **Well‑structured**: Clear directories, scripts, and environment setup

### Executive Summary
- Median house value is positively associated with `MedInc` and proximity to coastal latitude/longitude bands.
- Correlations highlight `MedInc` as strongest single predictor among features provided.
- Regularized linear models perform similarly to OLS; tree‑based models (Random Forest, Gradient Boosting) often reduce RMSE further.
- Target distribution is right‑skewed; consider log‑transform for alternative modeling.

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

Python version: 3.11 recommended.

### Cloud deployment
- Streamlit Community Cloud (no code changes):
  - Go to `streamlit.io/cloud` → New app → point to this repo → set app path to `app/streamlit_app.py` → deploy.
- Render (one-click using `render.yaml`):
  - Create account at `render.com`, new Web Service from repo → it will auto-detect `render.yaml` → deploy. Start command uses Streamlit with `$PORT`.
- Heroku/Railway (Procfile included):
  - Set buildpacks for Python, deploy. The `Procfile` runs Streamlit bound to `$PORT`.

### Dataset
The California Housing dataset is loaded via `sklearn.datasets.fetch_california_housing`. No external download is needed. Target is `MedHouseVal`; features include `MedInc`, `HouseAge`, `AveRooms`, `AveBedrms`, `Population`, `AveOccup`, `Latitude`, and `Longitude`.

### What’s inside the notebook
- Data overview and sanity checks (shape, types, missing values)
- Descriptive statistics and target analysis (skew, outliers)
- Feature distributions and correlation heatmap
- Simple geospatial scatter by latitude/longitude
- Baseline regressors and evaluation (e.g., MAE, RMSE, R²)

### Selected Visuals
![Target distribution](reports/figures/target_hist.png)
![Correlation heatmap](reports/figures/correlation_heatmap.png)

### Reproducing results
All results can be reproduced by running the scripts and/or opening `notebooks/01_eda_california_housing.ipynb`. To create a shareable report, use `make report` which converts the notebook to HTML via `nbconvert`.

### Requirements
See `requirements.txt` for pinned packages. Key libraries:
- pandas, numpy, matplotlib, seaborn
- scikit‑learn
- jupyter, nbconvert

Conda users can use `environment.yml`.

### License
This project is released under the MIT License. See `LICENSE` for details.

### Interactive Demo (optional)
Run a simple Streamlit app locally:
```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

### Acknowledgments
Dataset provided by `scikit‑learn`. Inspiration: common EDA and baseline modeling workflows for tabular regression problems.