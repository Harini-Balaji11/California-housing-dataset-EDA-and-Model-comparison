import os
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import fetch_california_housing


def ensure_output_dirs() -> Path:
    reports_dir = Path("reports")
    figures_dir = reports_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    return figures_dir


def load_data() -> pd.DataFrame:
    data = fetch_california_housing(as_frame=True)
    return data.frame


def plot_target_distribution(df: pd.DataFrame, out: Path) -> None:
    plt.figure(figsize=(8, 6))
    sns.histplot(df["MedHouseVal"], kde=True, bins=30, color="crimson")
    plt.title("Distribution of Median House Value")
    plt.xlabel("Median House Value ($100,000s)")
    plt.tight_layout()
    plt.savefig(out / "target_hist.png", dpi=150)
    plt.close()


def plot_correlation_heatmap(df: pd.DataFrame, out: Path) -> None:
    plt.figure(figsize=(9, 7))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=False, cmap="coolwarm", center=0)
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(out / "correlation_heatmap.png", dpi=150)
    plt.close()


def plot_geo_scatter(df: pd.DataFrame, out: Path) -> None:
    plt.figure(figsize=(8, 6))
    sc = plt.scatter(
        df["Longitude"],
        df["Latitude"],
        c=df["MedHouseVal"],
        cmap="viridis",
        alpha=0.6,
        s=8,
    )
    plt.colorbar(sc, label="MedHouseVal ($100,000s)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("California Housing: Geo Scatter by Median Value")
    plt.tight_layout()
    plt.savefig(out / "geo_scatter.png", dpi=150)
    plt.close()


def main() -> None:
    figures_dir = ensure_output_dirs()
    df = load_data()

    # Basic sanity outputs
    print("Dataset shape:", df.shape)
    print(df.describe().T)

    # Plots
    plot_target_distribution(df, figures_dir)
    plot_correlation_heatmap(df, figures_dir)
    plot_geo_scatter(df, figures_dir)

    print(f"Saved figures to: {figures_dir}")


if __name__ == "__main__":
    main()


