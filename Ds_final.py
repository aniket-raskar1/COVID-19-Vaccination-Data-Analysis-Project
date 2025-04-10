import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="COVID Vaccination India", layout="wide")

st.title("💉 COVID-19 Vaccination Data Analysis - India")

# Load and clean dataset
df = pd.read_csv("Dataset\covid_vaccine_statewise.csv")
df.columns = df.columns.str.strip()  # Remove any leading/trailing whitespace

# Show raw data if checkbox selected
if st.checkbox("Show raw data"):
    st.dataframe(df)

# Display stats in columns
st.subheader("📊 Overall Vaccination Statistics")

col1, col2, col3 = st.columns(3)
col1.metric("👨‍🦱 Total Males Vaccinated", f"{int(df['Male_count'].sum()):,}")
col2.metric("👩‍🦱 Total Females Vaccinated", f"{int(df['Female_count'].sum()):,}")
col3.metric("🧑‍🤝‍🧑 Total Individuals Vaccinated", f"{int(df['Total Individuals Vaccinated'].sum()):,}")

# First and second dose by state
st.subheader("📍 Vaccination Dose Distribution by State")

first_dose_by_state = df.groupby('State')['First Dose Administered'].sum().sort_values(ascending=False)
second_dose_by_state = df.groupby('State')['Second Dose Administered'].sum().sort_values(ascending=False)

tab1, tab2 = st.tabs(["1️⃣ First Dose", "2️⃣ Second Dose"])

with tab1:
    st.bar_chart(first_dose_by_state)

with tab2:
    st.bar_chart(second_dose_by_state)

# Vaccine type distribution
st.subheader("💉 Vaccine Type Distribution")

vaccine_cols = ['Covaxin (Doses Administered)', 'CoviShield (Doses Administered)', 'Sputnik V (Doses Administered)']
vaccine_data = df[vaccine_cols].sum().sort_values(ascending=False)

st.bar_chart(vaccine_data)

# Age group data
st.subheader("📈 Age Group-wise Vaccination")

age_group_cols = [
    '18-44 Years(Individuals Vaccinated)',
    '45-60 Years(Individuals Vaccinated)',
    '60+ Years(Individuals Vaccinated)'
]
age_data = df[age_group_cols].sum()

st.bar_chart(age_data)

# Footer
st.markdown("---")
st.caption("Created by Aniket Ashok Raskar | Data Source: [Kaggle - COVID19 in India Dataset](https://www.kaggle.com/sudalairajkumar/covid19-in-india)")
