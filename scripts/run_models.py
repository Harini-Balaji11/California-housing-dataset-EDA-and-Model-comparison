from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data() -> tuple[pd.DataFrame, pd.Series]:
    data = fetch_california_housing(as_frame=True)
    df = data.frame
    X = df.drop(columns=["MedHouseVal"])
    y = df["MedHouseVal"]
    return X, y


def evaluate_model(name: str, y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return {"model": name, "RMSE": rmse, "MAE": mae, "R2": r2}


def main() -> None:
    reports_dir = Path("reports")
    reports_dir.mkdir(parents=True, exist_ok=True)

    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Scale linear models' features for stability
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    models = [
        ("LinearRegression", LinearRegression(), True),
        ("Ridge", Ridge(alpha=1.0, random_state=42), True),
        ("Lasso", Lasso(alpha=0.001, random_state=42, max_iter=10000), True),
        ("RandomForest", RandomForestRegressor(n_estimators=300, random_state=42), False),
        ("GradientBoosting", GradientBoostingRegressor(random_state=42), False),
    ]

    results: list[dict] = []

    for name, model, use_scaled in models:
        if use_scaled:
            model.fit(X_train_scaled, y_train)
            preds = model.predict(X_test_scaled)
        else:
            model.fit(X_train, y_train)
            preds = model.predict(X_test)

        results.append(evaluate_model(name, y_test, preds))

    results_df = pd.DataFrame(results).sort_values("RMSE")
    print(results_df.to_string(index=False))
    results_df.to_csv(reports_dir / "model_comparison.csv", index=False)
    print(f"Saved metrics to {reports_dir / 'model_comparison.csv'}")


if __name__ == "__main__":
    main()


