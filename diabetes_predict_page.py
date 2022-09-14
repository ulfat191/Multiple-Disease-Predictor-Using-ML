import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps_diabetes.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

model1_loaded = data["model"]

def show_diabetes_predict_page():
    st.title("Multiple Disease Prediction - Diabetes Prediction")

    st.write("""### Please answer the questions below:  (move the slidebar to give correct value)""")

    Pregnancies = st.slider(
        "Total number of times pregnant", 0, 17, 1)

    Glucose = st.slider(
        "Glucose amount in blood", 1, 300, 1)

    BloodPressure = st.slider(
        "Blood pressure value", 1, 200, 1)

    SkinThickness = st.slider(
        "Thickness of the patient skin", 0, 100, 1)

    Insulin = st.slider(
        "Insulin amound intake", 0, 200, 0)

    BMI = st.number_input(
    "Body mass Index",
    min_value=1.0,
    max_value=50.0,
    step=0.1,
    format="%.2f")

    st.write(BMI)   

    DiabetesPedigreeFunction = st.number_input(
    "Likelihood of diabetes based on family history",
    min_value=0.001,
    max_value=10.0,
    step=0.001,
    format="%.3f")

    st.write(DiabetesPedigreeFunction)   

    Age = st.slider(
        "Age of the patient", 1, 120, 1)

    ok = st.button("Calculate Diabetes")

    if ok:
        X = np.array([[
            Pregnancies,
            Glucose,
            BloodPressure,
            SkinThickness,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age,
        ]])

        state = model1_loaded.predict(X)
        if state[0] == 0:
            st.subheader("No Diabetes.")
        elif state[0] == 1:
            st.subheader("Diabetic Patient.")
