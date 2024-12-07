import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Simulated data
st.title("Hospital Resource Management Dashboard")
data = {
    'Hour': [i for i in range(24)],
    'Patients Admitted': np.random.randint(5, 10, 24),
    'Staff Available': np.random.randint(5, 15, 24),
}
df = pd.DataFrame(data)

# Line chart for patients admitted
st.subheader("Patients Admitted Per Hour")
fig1 = px.line(df, x='Hour', y='Patients Admitted', title="Patients Admitted Per Hour")
st.plotly_chart(fig1)

# Bar chart for staff availability
st.subheader("Staff Availability Per Hour")
fig2 = px.bar(df, x='Hour', y='Staff Available', title="Staff Availability Per Hour")
st.plotly_chart(fig2)

# Text box for hospital updates
st.subheader("Hospital Updates")
st.text("Emergency Room: Average wait time - 15 mins\nPharmacy: Fully stocked\nPediatrics: Staff available - 3 doctors")