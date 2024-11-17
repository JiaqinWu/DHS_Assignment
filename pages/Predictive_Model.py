import streamlit as st
import joblib
import pandas as pd
import pickle

# Load the saved model
kmeans_model = joblib.load('kmeans_model.pkl')

# Define user inputs
st.title("Assistance Classification Dashboard")
st.write("Enter the details below to predict assistance needs:")

# Input fields for each feature
gender = st.selectbox("Gender", options=["Male", "Female"])
medicaid = st.selectbox("Enrolled in Medicaid CY2017", options=["Yes", "No"])
training = st.selectbox("Participated in Employment & Training Program in CY2017", options=["Yes", "No"])
earnings = [st.number_input(f"Earnings for {q}", value=0) for q in ["CY2017Q4", "CY2018Q1", "CY2018Q2", "CY2018Q3", "CY2018Q4", "CY2019Q1", "CY2019Q2","CY2019Q3"]]

# Convert categorical inputs to binary
gender_binary = 1 if gender == "Male" else 0
medicaid_binary = 1 if medicaid == "Yes" else 0
training_binary = 1 if training == "Yes" else 0

# Prepare input data
input_data = [gender_binary, medicaid_binary, training_binary] + earnings
input_df = pd.DataFrame([input_data], columns=['GENDER_Male', 'Enrolled in Medicaid CY2017_Y', 'Participated in Employment & Training Program in CY2017_Y'] + 
                        ["Earning_CY2017Q4", "Earning_CY2018Q1", "Earning_CY2018Q2", 
                         "Earning_CY2018Q3", "Earning_CY2018Q4", "Earning_CY2019Q1", "Earning_CY2019Q2","Earning_CY2019Q3"])

# Make predictions
if st.button("Predict"):
    cluster = kmeans_model.predict(input_df)
    if cluster[0] == 0:
        st.success("This individual is more likely to need assistance.")
    else:
        st.success("This individual is less likely to need assistance.")
