import joblib
import numpy as np

class DiseasePredictor:
    def __init__(self):
        self.model = joblib.load("model/disease_model.pkl")
        self.encoder = joblib.load("model/symptom_encoder.pkl")

    def predict(self, symptoms):
        cleaned_symptoms = [
            symptom.strip().lower().replace(" ", "_")
            for symptom in symptoms
        ]

        input_data = self.encoder.transform([cleaned_symptoms])

        prediction = self.model.predict(input_data)[0]

        probabilities = self.model.predict_proba(input_data)[0]
        classes = self.model.classes_

        top_indices = np.argsort(probabilities)[::-1][:3]

        top_predictions = []

        for index in top_indices:
            top_predictions.append(
                {
                    "disease": classes[index],
                    "probability": probabilities[index] * 100
                }
            )

        return prediction, top_predictions
