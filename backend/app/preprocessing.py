import pandas as pd
import numpy as np
import json
import pickle


ARTIFACT_PATH = "app/artifacts"

with open(f"{ARTIFACT_PATH}/feature_columns.json", "r", encoding="utf-8") as f:
    FEATURE_COLUMNS = json.load(f)

with open(f"{ARTIFACT_PATH}/categorical_columns.json", "r", encoding="utf-8") as f:
    CAT_COLS = json.load(f)

with open(f"{ARTIFACT_PATH}/category_maps.pkl", "rb") as f:
    CATEGORY_MAPS = pickle.load(f)


def preprocess(df: pd.DataFrame) -> pd.DataFrame:

    for col in FEATURE_COLUMNS:
        if col not in df.columns:
            df[col] = np.nan

    for col in FEATURE_COLUMNS:
        if col not in CAT_COLS:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    for col in CAT_COLS:
        df[col] = df[col].astype("category")
        df[col] = df[col].cat.add_categories(["__MISSING__"]).fillna("__MISSING__")

    for col in FEATURE_COLUMNS:
        if col not in CAT_COLS:
            df[col] = df[col].fillna(df[col].median())

    return df[FEATURE_COLUMNS]