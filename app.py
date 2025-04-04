import streamlit as st
import pandas as pd

# Title
st.title("Heart Attack Risk Dashboard")

# Load Data
df = pd.read_csv("heart_attack_prediction_india.csv")

# Show Full Data
st.write("### Full Dataset", df)

# Gender-based Risk
st.write("### Average Heart Attack Risk by Gender")
st.write(df.groupby("Gender")["Heart_Attack_Risk"].mean())

# --- New Section: Filter by Age and Gender ---
st.write("---")
st.write("### Search by Age and Gender")

# Input fields
age_input = st.number_input("Enter Age", min_value=0, max_value=120, step=1)
gender_input = st.text_input("Enter Gender (e.g., Male or Female)")

# Filter the data only if gender is entered
if gender_input:
    filtered_data = df[
        (df["Age"] == age_input) &
        (df["Gender"].str.lower() == gender_input.lower())
    ]
    st.write("### Filtered Results")
    
    if not filtered_data.empty:
        st.dataframe(filtered_data)

        # Show unique states from the filtered result
        unique_states = filtered_data.drop_duplicates(subset="State_Name")
        st.write("### States from Result")
        st.write(unique_states["State_Name"].reset_index(drop=True))
    else:
        st.warning("No data found for the given Age and Gender.")
