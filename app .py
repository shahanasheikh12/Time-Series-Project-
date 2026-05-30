
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from statsmodels.tsa.arima.model import ARIMA

# Title

st.title("⚡ Electric Production Forecast Dashboard")

# Load dataset

df = pd.read_csv("Electric_Production.csv")

# Rename columns

df.columns = ['Date', 'Production']

# Convert date column

df['Date'] = pd.to_datetime(df['Date'])

# Set index

df.set_index('Date', inplace=True)

# Show dataset

st.subheader("Dataset")

st.write(df.head())

# Plot original data

st.subheader("Production Trend")

fig, ax = plt.subplots(figsize=(12,5))

ax.plot(df.index, df['Production'])

plt.xlabel("Date")
plt.ylabel("Production")

st.pyplot(fig)

# Load model

with open('forecast_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Forecast future values

forecast_steps = st.slider("Select Forecast Days", 1, 50, 12)

forecast = model.forecast(steps=forecast_steps)

# Create future dates

future_dates = pd.date_range(
    start=df.index[-1],
    periods=forecast_steps + 1,
    freq='M'
)[1:]

forecast_df = pd.DataFrame({
    'Date': future_dates,
    'Forecast': forecast
})

# Show forecast table

st.subheader("Forecast Data")

st.write(forecast_df)

# Plot forecast

st.subheader("Forecast Plot")

fig2, ax2 = plt.subplots(figsize=(12,5))

ax2.plot(df.index, df['Production'], label='Historical Data')

ax2.plot(
    forecast_df['Date'],
    forecast_df['Forecast'],
    label='Forecast',
    color='red'
)

plt.legend()

st.pyplot(fig2)
