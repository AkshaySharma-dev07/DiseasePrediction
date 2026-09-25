# Project Statement

## Project

Disease Prediction System Using Python and Machine Learning

## Problem Statement

Identifying diseases from many symptoms is hard. This project creates a learning tool that looks at selected symptoms and tells you a disease.

## Scope

The project focuses on:

- Loading and cleaning symptom data.

- Turning symptoms into numbers the machine can read.

- Teaching a machine‑learning model.

- Guessing disease classes when you pick symptoms.

- Showing results on a web page.

## Target Users

- Students who are learning Python and machine learning.

- People who want to show how symptoms can be classified.

- Teachers or reviewers who look at a Python ML project.

## High‑Level Features

1.. Clean the data set.

2. Pick out symptom numbers.

3. Teach the machine‑learning model.

4. Guess the disease.

5. Show the chance of the guess.

6. Use a Streamlit interface that's easy to use.

7. Check that inputs are good.

## Functional Requirements

### FR1: Dataset Loading

The system will load the data set that contains diseases and symptoms.

### FR2: Data Processing

The system will clean the symptom data. Change it into numbers the machine can read.

### FR3: Model Training

The system will teach a Random Forest model to classify diseases.

### FR4: Disease Prediction

The system will guess a disease when you choose symptoms.

### FR5: Result Display

The system will show the disease it guessed and the next best guesses.

### FR6: Input Validation

The system will stop guessing if you do not pick symptoms.

## Non‑Functional Requirements

### NFR1: Usability

The application will have an easy web page.

### NFR2: Performance

The model will give predictions fast without learning each time.

### NFR3: Reliability

The application will check user input before guessing.

### NFR4: Maintainability

The project will keep Python files, for loading data training the model making predictions and running the app.

### NFR5: Error Handling

The system will give messages when input is wrong or missing.

## Main Workflow

```text

User selects symptoms

↓

Input validation

↓

Symptom preprocessing

↓

Feature encoding

↓

Random Forest model

↓

Disease prediction

↓

3 predictions displayed

```