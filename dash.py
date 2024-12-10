import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random

# Title of the dashboard
st.title("Hospital Resource Management Dashboard")

# Simulated data for demonstration
data = {
    'Hour': [i for i in range(24)],
    'Patients Admitted': np.random.randint(5, 20, 24),
    'Staff Available': np.random.randint(5, 15, 24),
}
df = pd.DataFrame(data)

# Line chart for patient admissions
st.subheader("Patients Admitted Per Hour")
fig1 = px.line(df, x='Hour', y='Patients Admitted', title="Patients Admitted Per Hour")
st.plotly_chart(fig1)

# Bar chart for staff availability
st.subheader("Staff Availability Per Hour")
fig2 = px.bar(df, x='Hour', y='Staff Available', title="Staff Availability Per Hour")
st.plotly_chart(fig2)

# Patient updates
st.subheader("Updates for Patients")
st.write("""
- Emergency Room: Average wait time - 15 minutes  
- Pharmacy: Fully stocked  
- Pediatrics: Staff available - 3 doctors  
""")

# Simple form for patients to check wait time
st.subheader("Patient Portal")
name = st.text_input("Enter your name:")
if st.button("Check Wait Time"):
    # Generate a random wait time
    wait_time = random.randint(10, 60)  # Between 10 and 60 minutes
    st.write(f"Hello {name}, your estimated wait time is {wait_time} minutes.")


