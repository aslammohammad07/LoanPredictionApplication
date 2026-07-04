import joblib
import pandas as pd

MODEL_PATH = "ml/models/loan_model.pkl"
ENCODER_PATH = "ml/models/label_encoders.pkl"

model = joblib.load(MODEL_PATH)
encoders = joblib.load(ENCODER_PATH)


def predict_loan(data):

    input_df = pd.DataFrame([data])

    input_df["Gender"] = input_df["Gender"].str.capitalize()
    input_df["Married"] = input_df["Married"].str.capitalize()
    input_df["Education"] = input_df["Education"].str.capitalize()
    input_df["Self_Employed"] = input_df["Self_Employed"].str.capitalize()
    input_df["Property_Area"] = input_df["Property_Area"].str.capitalize()

    categorical_columns = [
        "Gender",
        "Married",
        "Dependents",
        "Education",
        "Self_Employed",
        "Property_Area"
    ]

    for column in categorical_columns:
        input_df[column] = encoders[column].transform(input_df[column])

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0].max()

    result = "Approved" if prediction == 1 else "Rejected"

    return result, float(probability)