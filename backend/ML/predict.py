import sys
import json
import joblib
import os

# Load model
model_path = os.path.join(os.path.dirname(__file__), 'risk_model.pkl')
model = joblib.load(model_path)

# Read input from Node.js
input_data = json.loads(sys.argv[1])

# Encode categorical features
risk_tolerance_map = {"Low": 0, "Moderate": 1, "High": 2}
investment_goal_map = {"retirement": 0, "education": 1, "wealth_growth": 2}
investment_experience_map = {"none": 0, "beginner": 1, "intermediate": 2, "expert": 3}
employment_status_map = {"unemployed": 0, "part_time": 1, "full_time": 2, "self_employed": 3}

# Format the feature vector
X = [[
    input_data["age"],
    input_data["income"],
    risk_tolerance_map[input_data["risk_tolerance"]],
    investment_goal_map[input_data["investment_goal"]],
    investment_experience_map[input_data["investment_experience"]],
    input_data["investment_duration"],
    input_data["debt_level"],
    input_data["savings"],
    input_data["dependents"],
    employment_status_map[input_data["employment_status"]]
]]

# Predict
prediction = model.predict(X)[0]

# Return prediction
print(json.dumps({ "prediction": prediction.item() }))


