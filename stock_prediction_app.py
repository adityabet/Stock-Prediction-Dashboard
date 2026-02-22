import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ta.momentum import RSIIndicator
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import datetime

st.set_page_config(page_title="Stock Prediction Dashboard", layout="wide")
st.title("Stock Market Prediction Dashboard")

stocks = {
    "Apple": "AAPL",
    "Tesla": "TSLA",
    "Microsoft": "MSFT",
    "Google": "GOOGL",
    "Amazon": "AMZN",
    "TCS (India)": "TCS.NS",
    "Reliance (India)": "RELIANCE.NS"
}

selected_stock = st.selectbox("Select Stock", list(stocks.keys()))

start = st.date_input("Start Date", datetime.date(2018,1,1))
end = st.date_input("End Date", datetime.date.today())

df = yf.download(stocks[selected_stock], start=start, end=end)

if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

df.reset_index(inplace=True)

if df.empty:
    st.error("No data found. Please change date range.")
    st.stop()

st.subheader("Latest Data")
st.dataframe(df.tail())

# MA
df['MA100'] = df['Close'].rolling(100).mean()
df['MA200'] = df['Close'].rolling(200).mean()

# RSI
rsi = RSIIndicator(close=df['Close'].squeeze(), window=14)
df['RSI'] = rsi.rsi()

def generate_signal(row):
    if row['MA100'] > row['MA200'] and row['RSI'] < 70:
        return "BUY"
    elif row['MA100'] < row['MA200'] and row['RSI'] > 30:
        return "SELL"
    else:
        return "HOLD"

df['Signal'] = df.apply(generate_signal, axis=1)
latest_signal = df['Signal'].iloc[-1]

st.subheader("Current Recommendation")
st.success(f"Signal: {latest_signal}")

st.subheader("Price with 100 & 200 MA")

plt.figure(figsize=(14,6))
sns.lineplot(x=df['Date'], y=df['Close'], label="Close Price")
sns.lineplot(x=df['Date'], y=df['MA100'], label="100 MA")
sns.lineplot(x=df['Date'], y=df['MA200'], label="200 MA")
plt.xticks(rotation=45)
plt.legend()
st.pyplot(plt)
plt.clf()

st.subheader("RSI Indicator")

plt.figure(figsize=(14,4))
sns.lineplot(x=df['Date'], y=df['RSI'])
plt.axhline(70)
plt.axhline(30)
plt.xticks(rotation=45)
st.pyplot(plt)
plt.clf()

# Yearly Return
st.subheader("Yearly Average Return")

df['Yearly_Return'] = df['Close'].pct_change(5)
yearly = df.groupby(df['Date'].dt.to_period("Y"))['Yearly_Return'].mean()

plt.figure(figsize=(14,6))
yearly.plot(kind='bar')
plt.xticks(rotation=90)
st.pyplot(plt)
plt.clf()

# Highest Daily Return
df['Daily_Return'] = df['Close'].pct_change()
highest_return = df['Daily_Return'].max()
best_day = df.loc[df['Daily_Return'].idxmax(), 'Date']

st.subheader("Highest Daily Return")
st.write(f"Highest Return: {round(highest_return*100,2)}% on {best_day.date()}")


st.subheader("Machine Learning Prediction (Next Day Price)")

# Next Day Prediction
df['Target'] = df['Close'].shift(-1)
df_ml = df[['Close','Target']].dropna()

X = df_ml[['Close']].values
y = df_ml['Target'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = r2_score(y_test, predictions)

st.write("Model R² Score:", round(accuracy*100,2), "%")

# Predict next day
last_price = np.array([[df['Close'].iloc[-1]]])
future_price = model.predict(last_price)

st.subheader("Predicted Next Day Price")
st.info(f"Predicted Price: {round(float(future_price),2)}")

# Actual vs Prediction
st.subheader("Actual vs Predicted")

plt.figure(figsize=(14,6))
plt.plot(y_test, label="Actual")
plt.plot(predictions, label="Predicted")
plt.legend()
st.pyplot(plt)
plt.clf()
