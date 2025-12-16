import pandas as pd
import shap
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def train_explainable_model(
    df: pd.DataFrame,
    target_col: str = "Close"
):
    """
    Train a tree-based model for explainability.
    """
    df = df.dropna()

    feature_cols = [
        col for col in df.columns
        if col not in [target_col, "Date", "Symbol", "Market_Regime"]
    ]

    X = df[feature_cols]
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=6,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model, X_train, X_test, feature_cols


def compute_shap_values(model, X_sample: pd.DataFrame):
    """
    Compute SHAP values for a trained model.
    """
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_sample)

    return explainer, shap_values


def get_feature_importance(
    shap_values,
    feature_names
) -> pd.DataFrame:
    """
    Aggregate SHAP values into feature importance.
    """
    importance = (
        abs(shap_values)
        .mean(axis=0)
    )

    return pd.DataFrame({
        "Feature": feature_names,
        "Importance": importance
    }).sort_values(by="Importance", ascending=False)
