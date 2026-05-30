# Electric Production Demand Forecasting

A Time Series Forecasting project built using ARIMA, Python, and Streamlit to predict future electric production demand. This project performs data preprocessing, visualization, trend analysis, forecasting, and deployment of an interactive dashboard.

---

# Project Overview

This project analyzes historical electric production data and forecasts future demand using Time Series Analysis techniques. The application provides visual insights into production trends and future predictions through an interactive Streamlit dashboard.

---

# Features

* Time Series Forecasting using ARIMA
* Interactive Streamlit Dashboard
* Data Cleaning and Preprocessing
* Trend Visualization
* Future Demand Prediction
* Forecast Accuracy Evaluation
* Streamlit Cloud Deployment

---

# Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Statsmodels
* Scikit-learn
* Streamlit

---

# Project Structure

```bash
Electric-Production-Forecasting/
│
├── app.py
├── Electric_Production.csv
├── forecast_model.pkl
├── requirements.txt
├── README.md
└── Time_series_Project.ipynb
```

---

# Dataset

The dataset contains historical electric production records over time.

Columns:

* Date
* Production

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Electric-Production-Forecasting.git
```

Move to the project folder:

```bash
cd Electric-Production-Forecasting
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run Streamlit App

```bash
streamlit run app.py
```

---

# Deployment

The project is deployed using Streamlit Community Cloud.

---

# Forecasting Model

This project uses the ARIMA Time Series model for forecasting future electric production demand.

ARIMA captures:

* Trends
* Seasonality
* Temporal dependencies

---

# Dashboard Features

* Historical Production Trend
* Future Forecast Visualization
* Forecast Table
* Interactive Forecast Slider
  
---
# Screenshots
## 1. Dashboard Overview

This screenshot displays the main interface of the Electric Production Forecast Dashboard developed using Streamlit. It includes a preview of the dataset, historical electric production trends, and an interactive slider that allows users to select the number of forecast periods. The graph visualizes production patterns over time and highlights seasonal fluctuations in electricity production.
<img width="696" height="847" alt="image" src="https://github.com/user-attachments/assets/3771634b-d2ff-4334-9ca2-439f37cfff7b" />


---

## 2. Forecast Results

This screenshot shows the forecasting section of the dashboard. It contains a table of predicted production values along with a forecast visualization plot. The blue line represents historical production data, while the red line indicates forecasted future production generated using the ARIMA time series forecasting model.
<img width="624" height="813" alt="image" src="https://github.com/user-attachments/assets/fd1b17a1-09e8-40bc-a7c7-3e8ed913cb7e" />

---

# Future Improvements

* Prophet Forecasting
* LSTM Deep Learning Model
* Real-time Forecasting
* Plotly Interactive Charts
* User Dataset Upload
* Dark Mode Dashboard

---

# Author

Developed by [Shahana Sheikh ]

---

# License

This project is open-source and available under the MIT License.
