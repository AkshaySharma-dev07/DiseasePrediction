import streamlit as st

from predictor import DiseasePredictor

st.set_page_config(
    page_title="Disease Prediction System",
    page_icon="🩺",
    layout="wide"
)

@st.cache_resource
def load_predictor():
    return DiseasePredictor()

predictor = load_predictor()

st.title("🩺 Disease Prediction System")
st.write(
    "Select your symptoms and the machine-learning model "
    "will generate a predicted disease."
)

st.warning(
    "This Project Is Made By Akshay Sharma (A B.Tech Student Of Branch CSE Core ) And This Is Based On A Dataset And Should Be Consulted By a Physician Before Taking And Serious Actions. This  "
    "diagnosis should not replace a qualified healthcare professionals Advice."
)

symptoms = list(predictor.encoder.classes_)

selected_symptoms = st.multiselect(
    "Select your symptoms:",
    symptoms,
    placeholder="Choose one or more symptoms..."
)

if st.button("🔍 Predict Disease", type="primary"):

    if len(selected_symptoms) < 2:
        st.error("Please select at least 2 symptoms.")
    else:
        prediction, top_predictions = predictor.predict(selected_symptoms)

        st.success(f"Predicted Disease: {prediction.replace('_', ' ').title()}")

        st.subheader("Top Predictions")

        for item in top_predictions:
            disease = item["disease"].replace("_", " ").title()
            probability = item["probability"]

            st.write(f"**{disease}** — {probability:.2f}%")
            st.progress(min(int(probability), 100))

st.divider()

st.caption(
    "Disease Prediction System | Python + Pandas + NumPy + Scikit-learn + Streamlit"
)
