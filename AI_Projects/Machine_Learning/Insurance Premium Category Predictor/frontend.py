import streamlit as st
import requests

# FastAPI ka URL
API_URL = "http://127.0.0.1:8000/predict" 

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below to predict your insurance category.")

# Input fields - Spelling 'weight' sahi ki gayi hai
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weigth = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):
    # Dictionary keys wahi honi chahiye jo FastAPI ke UserInput model mein hain
    input_data = {
        "age": age,
        "weigth": weigth,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "occupation": occupation
    }

    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        # Status check aur response parsing ko sahi kiya gaya hai
        if response.status_code == 200:
            # FastAPI prediction_category key bhejta hai
            prediction = result.get("prediction_category")
            st.success(f"Predicted Insurance Premium Category: **{prediction}**")
            
            # Note: Agar aapne confidence/probabilities return nahi ki hain FastAPI se, 
            # toh wo yahan display nahi hongi.
        else:
            st.error(f"API Error: {response.status_code}")
            st.json(result) # Error detail dekhne ke liye

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running (uvicorn).")