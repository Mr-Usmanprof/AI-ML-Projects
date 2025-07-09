from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model
model = joblib.load("model/churn_model.pkl")

# Pydantic model
class ChurnInput(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int
    MonthlyCharges: float
    TotalCharges: float
    HasPhone: int

@app.post("/predict")
def predict_churn(data: ChurnInput):
    try:
        input_array = np.array([list(data.dict().values())])
        prediction = model.predict(input_array)[0]
        return {"churn": int(prediction)}
    except Exception as e:
        return {"error": str(e)}

# ✅ Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "FastAPI is running"}


