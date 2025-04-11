import pickle
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_model(model_path="sub_agents/forecast/linear_regression_model.pkl"):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    with open("sub_agents/forecast/scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
        return model, scaler    


def predict_price(file_path="sub_agents/forecast/model_data.csv"):
    model, scaler = load_model()
    # Set target date as today
    target_date = pd.to_datetime(datetime.now().strftime("%Y-%m-%d"))
    target_year = target_date.year
    target_month = target_date.month

    # Load and prepare data
    data = pd.read_csv(file_path)
    data["Date"] = pd.to_datetime(data["Date"])


    # Filter only rows from the current month and year
    current_month_data = data[
        (data["Date"].dt.year == target_year) &
        (data["Date"].dt.month == target_month)
    ].sort_values("Date")

    if current_month_data.empty:
        raise ValueError("No data available for the current month.")
    latest = current_month_data.iloc[-1]
    feature_cols = ['GDP_lag1', 'IR_lag1', 'Unemployment_lag1', 'Close_lag1', 'Volume_lag1', 'HPI_ma_3', 'HPI_lag1']

    
    features = latest[feature_cols].values.reshape(1, -1)
    features = scaler.transform(features)
   
    predicted_price = model.predict(features)
    return predicted_price[0][0]


def generate_forecast_plots(file_path="sub_agents/forecast/model_data.csv"):
    # Load historical data
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])

    # Predict today's HPI
    predicted_hpi = predict_price(file_path)
    today = pd.to_datetime(datetime.now().strftime("%Y-%m-%d"))

    # Prepare HPI plot
    fig_hpi, ax1 = plt.subplots(figsize=(8, 4))
    sns.lineplot(data=df, x="Date", y="HPI_lag1", label="Historical HPI", ax=ax1)
    ax1.scatter([today], [predicted_hpi], color="red", label="Predicted HPI")
    ax1.set_title("HPI Trend + Prediction")
    ax1.legend()
    ax1.set_ylabel("HPI")
    ax1.set_xlabel("Date")

    # Interest Rate Plot
    fig_ir, ax2 = plt.subplots(figsize=(8, 4))
    sns.lineplot(data=df, x="Date", y="IR_lag1", ax=ax2)
    ax2.set_title("Historical Interest Rates")
    ax2.set_ylabel("Interest Rate (%)")
    ax2.set_xlabel("Date")

    # GDP Plot
    fig_gdp, ax3 = plt.subplots(figsize=(8, 4))
    sns.lineplot(data=df, x="Date", y="GDP_lag1", ax=ax3)
    ax3.set_title("Historical GDP")
    ax3.set_ylabel("GDP (lagged)")
    ax3.set_xlabel("Date")

    return fig_hpi, fig_ir, fig_gdp


def generate_forecast_data(file_path="sub_agents/forecast/model_data.csv"):
    # Load data
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])

    # Predict today's HPI
    predicted_hpi = predict_price(file_path)
    today = pd.to_datetime(datetime.now().strftime("%Y-%m-%d"))
    latest_entry = {
        "Date": today,
        "HPI_lag1": predicted_hpi,
        "IR_lag1": None,
        "GDP_lag1": None
    }
    df = pd.concat([df, pd.DataFrame([latest_entry])], ignore_index=True)
    df.set_index("Date", inplace=True)
    hpi_data = df[["HPI_lag1"]].rename(columns={"HPI_lag1": "HPI (including prediction)"})
    ir_data = df[["IR_lag1"]].dropna().rename(columns={"IR_lag1": "Interest Rate"})
    gdp_data = df[["GDP_lag1"]].dropna().rename(columns={"GDP_lag1": "GDP"})

    return hpi_data, ir_data, gdp_data
