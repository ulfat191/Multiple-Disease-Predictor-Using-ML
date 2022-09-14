import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps_parkinsons.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

model_loaded = data["model"]


def show_parkinsons_predict_page():
    st.title("Multiple Disease Prediction - Parkinsons Prediction")

    st.write("""### Please answer the questions below:  (move the slidebar to give correct value)""")

    MDVP1 = st.slider('MDVP:Fo(Hz)', 88.333, 260.105, 150.0)
    MDVP2 = st.slider('MDVP:Fhi(Hz)', 102.145, 592.030, 150.0)
    MDVP3 = st.slider('MDVP:Flo(Hz)', 65.476, 239.170, 150.0)
    MDVP4 = st.slider('MDVP:Jitter(%)', 0.006, 0.052, 0.001)
    MDVP5 = st.slider('MDVP:Jitter(Abs)', 0.000, 0.007, 0.001)
    MDVP6 = st.slider('MDVP:RAP', 0.003, 0.042, 0.001)
    MDVP7 = st.slider('MDVP:PPQ', 0.005, 0.051, 0.001)
    Jitter_DDP = st.slider('Jitter:DDP', 0.009, 0.123, 0.001)
    MDVP8 = st.slider('MDVP:Shimmer', 0.027, 0.169, 0.001)
    MDVP9 = st.slider('MDVP:Shimmer(dB)', 0.148, 0.991, 0.001)
    Shimmer_APQ3 = st.slider('Shimmer:APQ3', 0.020, 0.137, 0.001)
    Shimmer_APQ5 = st.slider('Shimmer:APQ5', 0.010, 0.119, 0.001)
    MDVP10 = st.slider('MDVP:APQ', 0.018, 0.137, 0.001)
    Shimmer_DDA = st.slider('Shimmer:DDA', 0.048, 0.268, 0.001)
    NHR = st.slider('NHR', 0.000, 0.314, 0.001)
    HNR = st.slider('HNR', 0.000, 33.047, 0.001)
    RPDE = st.slider('RPDE', 0.000, 1.000, 0.001)
    DFA = st.slider('DFA', 0.000, 1.000, 0.001)
    spread1 = st.slider('spread1', 0.000, 1.000, 0.001)
    spread2 = st.slider('spread2', 0.000, 1.000, 0.001)
    D2 = st.slider('D2', 0.000, 1.000, 0.001)
    PPE = st.slider('PPE', 0.000, 1.000, 0.001)
    ok = st.button("Calculate Parkinsons Prediction")
    if ok:
        X = np.array([[
            MDVP1,
            MDVP2,
            MDVP3,
            MDVP4,
            MDVP5,
            MDVP6,
            MDVP7,
            Jitter_DDP,
            MDVP8,
            MDVP9,
            Shimmer_APQ3,
            Shimmer_APQ5,
            MDVP10,
            Shimmer_DDA,
            NHR,
            HNR,
            RPDE,
            DFA,
            spread1,
            spread2,
            D2,
            PPE
        ]])

        state = model_loaded.predict(X)
        if state[0] == 0:
            st.subheader("No Parkinson's Disease.")
        elif state[0] == 1:
            st.subheader("Has Parkinson's Disease.")

