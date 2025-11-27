from fastapi import FastAPI, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

from app.inference import predict_df
from app.retrain import retrain_model


app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok", "message": "Fraud ML API running"}


@app.post("/predict")
async def predict_csv(
    file: UploadFile = File(...),
    threshold: float = Query(0.02, description="Model response threshold"),
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