# Disease Prediction System

A machine-learning-based web application that predicts a possible
disease from user-provided symptoms.

## Features

-   Interactive web interface built with Streamlit
-   Symptom-based disease prediction
-   Trained disease prediction model
-   Symptom encoding for model input
-   CSV-based dataset
-   Separate modules for data loading, model handling, and prediction

## Project Structure

``` text
DiseasePrediction/
├── data/
│   └── dataset.csv
├── model/
│   ├── disease_model.pkl
│   └── symptom_encoder.pkl
├── docs/
├── tests/
├── apps.py
├── data_loader.py
├── model.py
├── predictor.py
├── requirements.txt
├── README.md
└── statement.md
```

## Technologies Used

-   Python
-   Streamlit
-   Machine Learning
-   Pandas
-   NumPy
-   Scikit-learn

## How to Run

### 1. Clone the repository

``` bash
git clone https://github.com/AkshaySharma-dev07/DiseasePrediction.git
cd DiseasePrediction
```

### 2. Create a virtual environment

``` bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

``` powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

``` bash
python -m pip install -r requirements.txt
```

### 5. Run the application

``` bash
python -m streamlit run apps.py
```

Streamlit will display a local URL in the terminal. Open that URL in a
web browser to use the application.

## How It Works

1.  The user provides symptoms through the web interface.
2.  The symptoms are processed and encoded.
3.  The trained machine-learning model uses the processed input.
4.  The application displays the predicted disease.

## Project Purpose

The project demonstrates how machine learning can be integrated with a
simple web interface to create an interactive symptom-based disease
prediction system.

## Note

This project is intended for educational and demonstration purposes. Its
predictions should not be treated as a medical diagnosis or a substitute
for professional medical advice.