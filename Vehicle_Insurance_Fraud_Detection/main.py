from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

with open('best_fraud_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model_columns.pkl', 'rb') as f:
    model_columns = pickle.load(f)

class ClaimData(BaseModel):
    features: Dict[str, object]

@app.post("/predict")
def predict(data: ClaimData):
    input_df = pd.DataFrame([data.features])
    
    input_df = input_df.reindex(columns=model_columns, fill_value=0)
    
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    
    return {
        "is_fraud": int(prediction),
        "confidence": float(probability),
        "result": "Fraud" if prediction == 1 else "Not Fraud"
    }