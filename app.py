import streamlit as st
import pandas as pd

# Title
st.title("Heart Attack Risk Dashboard")

# Load Data
df = pd.read_csv("heart_attack_prediction_india.csv")

# Show Data
st.write(df)

# Gender-based Risk
st.write("### Average Heart Attack Risk by Gender")
st.write(df.groupby("Gender")["Heart_Attack_Risk"].mean())