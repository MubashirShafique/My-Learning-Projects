import streamlit as st
import joblib
import pandas as pd

# Page setup
st.set_page_config(page_title="Salary Predictor", layout="centered")
st.header("Salary Prediction")
st.write("Select features according to your career")

# Input fields
col1, col2 = st.columns(2)

with col1:
    job_title = st.selectbox("Job Title", ["Backend Developer", "Cybersecurity Analyst", "Product Manager", "AI Engineer", "Data Scientist", "DevOps Engineer", "Software Engineer", "Data Analyst", "Cloud Engineer", "Machine Learning Engineer", "Business Analyst", "Frontend Developer"])
    education_level = st.selectbox("Education Level", ["Master", "High School", "Bachelor", "PhD", "Diploma"])
    industry = st.selectbox("Industry", ["Finance", "Consulting", "Media", "Manufacturing", "Technology", "Government", "Healthcare", "Education", "Telecom", "Retail"])
    company_size = st.selectbox("Company Size", ["Large", "Small", "Medium", "Enterprise", "Startup"])

with col2:
    location = st.selectbox("Location", ["Australia", "Canada", "Sweden", "Remote", "Singapore", "USA", "UK", "India", "Netherlands", "Germany"])
    remote_work = st.selectbox("Remote Work", ["Yes", "No", "Hybrid"])
    experience_level = st.select_slider("Experience Level (Years)", range(21))
    skills_count = st.select_slider("Skills Count", range(1, 20))

certifications = st.select_slider("Certifications Done", range(6))

# Load assets
@st.cache_resource
def load_models():
    encoder = joblib.load('encoder.joblib')
    model = joblib.load('model.joblib')
    columns = joblib.load("Columns.joblib")
    return encoder, model, columns

encoder, model, columns = load_models()

# Prediction logic
if st.button("Predict The Salary", use_container_width=True):
    # Categorical encoding
    cat_data = pd.DataFrame([[job_title, education_level, industry, company_size, location, remote_work]], 
                            columns=['job_title', 'education_level', 'industry', 'company_size', 'location', 'remote_work'])
    
    encoded_vals = encoder.transform(cat_data).toarray()
    encoded_df = pd.DataFrame(encoded_vals, columns=encoder.get_feature_names_out())

    # Numerical features
    num_df = pd.DataFrame([[experience_level, skills_count, certifications]], 
                          columns=['experience_years', 'skills_count', 'certifications'])

    # Final processing
    final_df = pd.concat([encoded_df, num_df], axis=1).reindex(columns=columns, fill_value=0)
    prediction = model.predict(final_df)

    st.success(f"Estimated Salary: **${int(prediction[0]):,}**")