import pandas as pd
from catboost import CatBoostClassifier, Pool
import json
import pickle

from app.preprocessing import FEATURE_COLUMNS, CAT_COLS, preprocess

MODEL_PATH = "app/models/catboost_fraud_model.cbm"


def retrain_model(df: pd.DataFrame) -> float:

    df_train = preprocess(df)
    y = df["target"].astype(int)

    cat_idx = [FEATURE_COLUMNS.index(c) for c in CAT_COLS]

    train_pool = Pool(df_train, y, cat_features=cat_idx)

    model = CatBoostClassifier(
        iterations=500,
        depth=6,
        learning_rate=0.05,
        loss_function="Logloss",
        eval_metric="AUC"
    )

    model.fit(train_pool)

    model.save_model(MODEL_PATH)

    return model.get_best_score()["learn"]["AUC"]