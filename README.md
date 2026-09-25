The Disease Prediction System is a Python-based machine learning application that predicts a possible disease from selected symptoms.

The system uses a Random Forest classification model trained on a dataset containing 4, 920 records, 41 diseases, and 131 unique symptoms.

This project was developed as an educational project to demonstrate Python programming, data processing, machine learning, modular programming, and a user interface.

> **Medical Disclaimer:** This project is for educational purposes only. It is not a medical diagnostic tool and should not replace advice from a qualified healthcare professional.

- Select multiple symptoms through a web interface.
- Process and clean symptom data.
- Predict a disease using a Random Forest classifier.
- Display the top three model predictions.
- Display prediction probabilities.
- Validate that the user selects enough symptoms.
- Modular Python project structure.
- Automated model training and model storage.

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib

```text
DiseasePrediction/
│
├── data/
│   └── dataset.csv
│
├── model/
│   ├── disease_model.pkl
│   └── symptom_encoder.pkl
│
├── tests/
│
├── docs/
│
├── app.py
├── data_loader.py
├── model.py
├── predictor.py
├── requirements.txt
├── statement.md
└── README.md
