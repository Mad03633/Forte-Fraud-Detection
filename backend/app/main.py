from fastapi import FastAPI, UploadFile, File, Query
import pandas as pd

from app.inference import predict_df
from app.retrain import retrain_model

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok", "message": "Fraud ML API running"}


@app.post("/predict")
async def predict_csv(
    file: UploadFile = File(...),
    threshold: float = Query(0.02, description="Порог срабатывания модели")
):
    df = pd.read_csv(file.file)
    result = predict_df(df, threshold)

    return result.to_dict(orient="records")


@app.post("/predict-row")
async def predict_row(row: dict, threshold: float = 0.02):

    df = pd.DataFrame([row])
    result = predict_df(df, threshold)

    return result.to_dict(orient="records")[0]


@app.post("/retrain")
async def retrain(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    auc = retrain_model(df)
    return {"status": "ok", "new_auc": auc}