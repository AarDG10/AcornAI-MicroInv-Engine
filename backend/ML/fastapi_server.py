from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import os

app = FastAPI()

app.add_middleware(   #have to add cors middleware
    CORSMiddleware,
    allow_origins=["*"],  # use ["http://localhost:5500"] if you're using Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    age: int
    income: float
    risk_tolerance: str
    investment_goal: str
    investment_experience: str
    investment_duration: int
    debt_level: float
    savings: float
    dependents: int
    employment_status: str

@app.post("/predict")
def predict(data: InputData):
    model_path = os.path.join(os.path.dirname(__file__), 'risk_model.pkl')
    model = joblib.load(model_path)

    risk_tolerance_map = {"Low": 0, "Moderate": 1, "High": 2}
    investment_goal_map = {"retirement": 0, "education": 1, "wealth_growth": 2}
    investment_experience_map = {"none": 0, "beginner": 1, "intermediate": 2, "expert": 3}
    employment_status_map = {"unemployed": 0, "part_time": 1, "full_time": 2, "self_employed": 3}

    X = [[
        data.age,
        data.income,
        risk_tolerance_map[data.risk_tolerance],
        investment_goal_map[data.investment_goal],
        investment_experience_map[data.investment_experience],
        data.investment_duration,
        data.debt_level,
        data.savings,
        data.dependents,
        employment_status_map[data.employment_status]
    ]]

    prediction = model.predict(X)[0]
    return { "prediction": prediction.item() }
