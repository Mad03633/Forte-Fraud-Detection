import json
import pandas as pd
from catboost import CatBoostClassifier

from app.preprocessing import preprocess, FEATURE_COLUMNS, CAT_COLS


MODEL_PATH = "app/models/catboost_fraud_model.cbm"

cat_model = CatBoostClassifier()
cat_model.load_model(MODEL_PATH)


def predict_df(df: pd.DataFrame, threshold: float = 0.02):

    df_prep = preprocess(df)
    proba = cat_model.predict_proba(df_prep)[:, 1]

    preds = (proba >= threshold).astype(int)

    out = df.copy()
    out["fraud_proba"] = proba
    out["fraud_pred"] = preds

    return out