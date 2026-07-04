import pandas as pd


def load_dataset(path):
    return pd.read_csv(path)


def clean_dataset(df):

    categorical_columns = [
        "Gender",
        "Married",
        "Dependents",
        "Self_Employed",
        "Loan_Amount_Term",
        "Credit_History"
    ]

    for column in categorical_columns:
        df[column] = df[column].fillna(df[column].mode()[0])

    df["LoanAmount"] = df["LoanAmount"].fillna(
        df["LoanAmount"].median()
    )

    return df