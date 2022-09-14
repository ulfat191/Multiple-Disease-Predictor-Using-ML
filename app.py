import streamlit as st
from diabetes_predict_page import show_diabetes_predict_page
from heart_disease_predict_page import show_heart_disease_predict_page
from parkinsons_predict_page import show_parkinsons_predict_page
from dev_page import show_dev_page


page = st.sidebar.selectbox("Choose option", ("Predict Diabetes", "Predict Heart Disease",  "Predict Parkinsons", "Explore"))

if page == "Predict Parkinsons":
    show_parkinsons_predict_page()
elif page == "Predict Heart Disease":
    show_heart_disease_predict_page()  
elif page == "Predict Diabetes":
    show_diabetes_predict_page()

else:
    show_dev_page()