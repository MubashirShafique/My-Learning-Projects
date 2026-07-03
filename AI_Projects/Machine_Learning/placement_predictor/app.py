import streamlit as st
import pickle
import numpy as np

# Load model
try:
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
except:
    model = None

st.title("Placement Predictor")

# Input fields
iq = st.number_input("Enter IQ", min_value=0.0)
cgpa = st.number_input("Enter CGPA", min_value=0.0, max_value=10.0)

# Prediction button
if st.button("Predict"):

    if model is None:
        st.error("Model could not be loaded!")
    else:
        features = np.array([[iq, cgpa]])
        prediction = model.predict(features)

        if prediction[0] == 1:
            st.success("The student is likely to get placed")
        else:
            st.error("The student is unlikely to get placed")