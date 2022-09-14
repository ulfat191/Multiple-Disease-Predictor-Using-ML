import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps_heart.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

model_loaded = data["model"]


def show_heart_disease_predict_page():
    st.title("Heart Disease Prediction")

    st.write("""### Please answer the questions below:  (move the slidebar to give correct value)""")

    age = st.slider(
        "Age of the patient", 1, 120, 1)

    sex = st.slider(
        "Gender(1= Male, 0= Female)", 0, 1, 1)

    cp = st.slider(
        "Chest pain type", 0, 3, 1)

    trestbps = st.slider(
        "Resting blood pressure", 90, 200, 1)

    chol = st.slider(
        "serum Cholesterol", 120, 550, 1)

    fbs = st.slider(
        "fasting blood sugar (1= True, 0= False)", 0, 1, 1)

    restecg = st.slider(
        "resting electrocardiographic results", 0, 2, 1)

    thalach = st.slider(
        "maximum heart rate achieved", 70, 205, 1)

    exang = st.slider(
        "exercise induced angina (1 = yes; 0 = no)", 0, 1, 1)

    oldpeak = st.number_input(
        "ST depression induced by exercise relative to rest",
        min_value=0.0,
        max_value=7.0,
        step=0.1,
        format="%.2f")

    st.write(oldpeak)

    slope = st.slider(
        "the slope of the peak exercise ST segment", 0, 2, 1)

    ca = st.slider(
        "number of major vessels (0-3) colored by flourosopy", 0, 3, 1)

    thal = st.slider(
        "1 = normal; 2 = fixed defect; 3 = reversable defect", 0, 3, 1)

    ok = st.button("Predict Heart Disease")

    if ok:
        X = np.array([[
            age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca,
            thal
        ]])

        state = model_loaded.predict(X)
        if state[0] == 0:
            st.subheader("No Heart Disease.")
        elif state[0] == 1:
            st.subheader("Has Heart Disease.")