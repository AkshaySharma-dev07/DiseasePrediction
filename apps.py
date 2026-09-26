import streamlit as st
import csv
from collections import Counter

st.set_page_config(
    page_title="Disease Prediction System",
    page_icon="🩺",
    layout="wide"
)


@st.cache_data
def load_dataset():
    with open("data/dataset.csv", "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def clean_symptom(symptom):
    return symptom.strip().lower().replace(" ", "_")


def get_all_symptoms(data):
    symptoms = set()

    for row in data:
        for key, value in row.items():
            if key.startswith("Symptom_") and value:
                symptoms.add(clean_symptom(value))

    return sorted(symptoms)


def predict_disease(selected_symptoms, data):
    selected = set(selected_symptoms)

    disease_scores = Counter()

    for row in data:
        disease = row["Disease"]

        row_symptoms = set()

        for key, value in row.items():
            if key.startswith("Symptom_") and value:
                row_symptoms.add(clean_symptom(value))

        matches = len(selected.intersection(row_symptoms))

        if matches > 0:
            disease_scores[disease] += matches

    if not disease_scores:
        return []

    results = disease_scores.most_common(3)

    total = sum(score for _, score in results)

    output = []

    for disease, score in results:
        percentage = (score / total) * 100
        output.append((disease, percentage))

    return output


# Load dataset
data = load_dataset()
symptoms = get_all_symptoms(data)


# -----------------------------
# USER INTERFACE
# -----------------------------

st.title("🩺 Disease Prediction System")

st.write(
    "Select your symptoms and the system will generate "
    "the most relevant disease predictions."
)

st.warning(
    "This Project Is Made By Akshay Sharma (A B.Tech Student Of Branch CSE Core ) And This Is Based On A Dataset And Should Be Consulted By a Physician Before Taking And Serious Actions. This  "
    "diagnosis should not replace a qualified healthcare professionals Advice. "
    
)

st.divider()

selected_symptoms = st.multiselect(
    "Select your symptoms:",
    symptoms,
    placeholder="Choose one or more symptoms..."
)


if st.button("🔍 Predict Disease", type="primary"):

    if len(selected_symptoms) < 2:

        st.error("Please select at least 2 symptoms.")

    else:

        results = predict_disease(selected_symptoms, data)

        if results:

            st.success(
                f"Predicted Disease: "
                f"{results[0][0].replace('_', ' ').title()}"
            )

            st.subheader("Top Predictions")

            for disease, probability in results:

                st.write(
                    f"**{disease.replace('_', ' ').title()}** "
                    f"— {probability:.2f}%"
                )

                st.progress(
                    min(int(probability), 100)
                )

        else:

            st.error(
                "No matching disease was found for the selected symptoms."
            )


st.divider()

st.caption(
    "Disease Prediction System | Python + CSV + Streamlit"
)