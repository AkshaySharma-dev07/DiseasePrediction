import os
import joblib
import pandas as pd

from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from data_loader import load_dataset, clean_dataset

def prepare_data(df):
    symptom_columns = [
        column for column in df.columns
        if column.startswith("Symptom_")
    ]

    symptom_lists = []

    for _, row in df.iterrows():
        symptoms = [
            row[column]
            for column in symptom_columns
            if row[column] != ""
        ]
        symptom_lists.append(symptoms)

    encoder = MultiLabelBinarizer()
    X = encoder.fit_transform(symptom_lists)
    y = df["Disease"]

    return X, y, encoder

def train_model():
    df = load_dataset()
    df = clean_dataset(df)

    X, y, encoder = prepare_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    os.makedirs("model", exist_ok=True)

    joblib.dump(model, "model/disease_model.pkl")
    joblib.dump(encoder, "model/symptom_encoder.pkl")

    print("Model trained successfully!")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print("Model saved successfully.")

if __name__ == "__main__":
    train_model()
