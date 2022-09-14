import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

def show_dev_page():
    st.title("Team Members")
    st.write("""### Md Ulfat Tahsin""")
    st.write("""### Sarah Jasim""")
    st.write("""### Mostafizur Rahman""")

    st.title("Supervisor")
    st.write("""### Mr. Intisar Tahmid Naheen""")

    st.title("Course")
    st.write("""### CSE445 Machine Learning""")

    st.title("Accuracy Metrics for Diabetes Disease Prediction")

    image1 = Image.open('logistic_regression.png')

    st.image(image1, caption='ROC AUC for Logistic Regression - Diabetes Prediction')

    image2 = Image.open('logistic regression CM.png')

    st.image(image2, caption='Confusion Matrix for Logistic Regression - Diabetes Prediction')

    st.title("Accuracy Metrics for Heart Disease Prediction")

    image1 = Image.open('decision_tree.png')

    st.image(image1, caption='ROC AUC for Decision Tree -  Heart Disease Prediction')

    image2 = Image.open('decision_tree CM.png')

    st.image(image2, caption='Confusion Matrix for Decision Tree -  Heart Disease Prediction')

    st.title("Accuracy Metrics for Parkinsons' Disease Prediction")

    image2 = Image.open('parkinson img.png')

    st.image(image2, caption='ROC -  Parkinsons Disease Prediction')
 
    st.title("Link to Github repository")
    st.write("check out this [link](https://github.com/imostafizur/CSE445_Multiple_Disease_Predictor)")

    st.title("Link to Project Report")
    st.write("check out this [link](https://drive.google.com/file/d/1B23ngry-xl6-KNtxKPKU8iG1dG6y8BtX/view?usp=sharinghttps://drive.google.com/file/d/1B23ngry-xl6-KNtxKPKU8iG1dG6y8BtX/view?usp=sharing)")