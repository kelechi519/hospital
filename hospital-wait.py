import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Generate data
data = {
    'hour': [i for i in range(24)],
    'patients_admitted': np.random.randint(5, 20, 24),
    'staff_available': np.random.randint(5, 15, 24)
}

# Create DataFrame
df = pd.DataFrame(data)

# Fit the Linear Regression model
model = LinearRegression()
model.fit(df[['patients_admitted', 'staff_available']], np.random.randint(10, 60, 24))

# Make predictions
predicted_wait_times = model.predict(df[['patients_admitted', 'staff_available']])

# Add predictions to the dataframe
df['predicted_wait_times'] = predicted_wait_times

# Display the dataframe in the Streamlit app
st.write("Data with Predictions:", df)

# Visualize the predicted wait times using a line chart
st.line_chart(df[['hour', 'predicted_wait_times']].set_index('hour'))

# Optional: Display a scatter plot of the input data vs. predicted wait times
st.write("Scatter Plot of Patients vs Predicted Wait Times")
st.scatter_chart(df[['patients_admitted', 'predicted_wait_times']])
