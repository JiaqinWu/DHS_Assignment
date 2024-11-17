import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the dataset
def load_data(file_path):
    return pd.read_csv(file_path)

# Path to your dataset
file_path = "DHS_final.csv"  
df = load_data(file_path)

# Title of the Dashboard
st.title("Earnings Distribution Analysis")

# Dropdown Selection for Earnings Columns
earnings_columns = [
    "Earning_CY2017Q4", "Earning_CY2018Q1", "Earning_CY2018Q2", 
    "Earning_CY2018Q3", "Earning_CY2018Q4", "Earning_CY2019Q1", "Earning_CY2019Q2"
]
selected_column = st.selectbox("Select Earnings Column for Analysis:", earnings_columns)

# Section for Density Plot Analysis
st.subheader(f"Density Plot Analysis for {selected_column}")

# Define categorical columns for density plot analysis
categorical_columns = {
    "Gender": "GENDER",
    "Enrolled in Medicaid": "Enrolled in Medicaid CY2017",
    "Employment Training": "Participated in Employment & Training Program in CY2017"
}

# Generate Density Plots for each categorical variable
for label, col in categorical_columns.items():
    st.write(f"Density Plot by {label}:")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.kdeplot(data=df, x=selected_column, hue=col, ax=ax, fill=True, common_norm=False, palette="Set2")
    ax.set_title(f"{selected_column} Distribution by {label}")
    ax.set_xlim(0, 30000)  # Corrected to set_xlim
    ax.set_xlabel("Earnings")
    ax.set_ylabel("Density")
    st.pyplot(fig)
