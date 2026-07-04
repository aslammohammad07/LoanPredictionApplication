import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from xgboost import XGBClassifier
from preprocess import load_dataset, clean_dataset

DATASET_PATH = "ml/dataset/loan_prediction.csv"

df = load_dataset(DATASET_PATH)
df = clean_dataset(df)

print("\nDataset Loaded Successfully")
print(df.head())

df.drop("Loan_ID", axis=1, inplace=True)

label_encoders = {}

categorical_columns = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Property_Area",
    "Loan_Status"
]

for column in categorical_columns:
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    label_encoders[column] = encoder

print("\nCategorical Encoding Completed")

X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTrain/Test Split Completed")

model = XGBClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=4,
    random_state=42,
    eval_metric="logloss"
)

print("\nTraining Started...")
model.fit(X_train, y_train)
print("Training Completed")

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n===============================")
print("MODEL PERFORMANCE")
print("===============================")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

MODEL_FOLDER = "ml/models"

os.makedirs(MODEL_FOLDER, exist_ok=True)

joblib.dump(model, os.path.join(MODEL_FOLDER, "loan_model.pkl"))
joblib.dump(label_encoders, os.path.join(MODEL_FOLDER, "label_encoders.pkl"))

print("\nModel Saved Successfully")
print("Location:", MODEL_FOLDER)