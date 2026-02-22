# AI-Powered Stock Market Prediction Dashboard

An advanced Stock Analysis and Machine Learning Web Application built using Python and Streamlit.

This project combines Technical Analysis, Trading Signals, Performance Metrics, and Machine Learning forecasting into one interactive dashboard.

---

## Project Overview

The Stock Market Prediction Dashboard provides:

- Real-time stock data using yFinance
- Moving Average (100 & 200 days) trend analysis
- RSI (Relative Strength Index) momentum indicator
- Automated BUY / SELL / HOLD signals
- Yearly average return analysis
- Highest daily return identification
- Machine Learning next-day price prediction
- Actual vs Predicted visualization

This project demonstrates practical application of:

- Financial data analysis
- Time-series modeling
- Feature engineering
- Supervised machine learning
- Interactive dashboard development

---

## Features

### 1. Stock Selection
Supports both US and Indian stocks:

- Apple (AAPL)
- Tesla (TSLA)
- Microsoft (MSFT)
- Google (GOOGL)
- Amazon (AMZN)
- TCS (India)
- Reliance (India)

---

### 2. Technical Indicators

Moving Averages:
- 100-Day Moving Average
- 200-Day Moving Average
- Golden Cross & Death Cross trend detection

RSI (14 Period):
- Overbought level: 70
- Oversold level: 30
- Momentum reversal insights

---

### 3. Smart Trading Signal Engine

Signal Logic:

BUY  → MA100 > MA200 AND RSI < 70  
SELL → MA100 < MA200 AND RSI > 30  
HOLD → Otherwise  

Displayed in real-time as the current recommendation.

---

### 4. Performance Analytics

- Yearly Average Return visualization
- Highest Daily Return detection
- Historical data display
- Volatility insight

---

### 5. Machine Learning Prediction

Model Used:
- Linear Regression
- Time-series based train-test split (80/20)
- R² Score evaluation

Outputs:
- Model accuracy (R² Score)
- Predicted Next-Day Closing Price
- Actual vs Predicted comparison graph

---

## Tech Stack

Backend & ML:
- Python
- Scikit-Learn
- Pandas
- NumPy

Visualization:
- Matplotlib
- Seaborn

Technical Indicators:
- TA Library

Frontend:
- Streamlit

Data Source:
- yFinance

---

## Project Structure

Stock_Prediction_App/
│
├── stock_prediction_app.py
├── requirements.txt
└── README.md

Main Application File:
stock_prediction_app.py

---

## Installation Guide

Step 1: Clone the Repository

git clone https://github.com/your-username/stock-prediction-dashboard.git
cd stock-prediction-dashboard

Step 2: Install Dependencies

pip install -r requirements.txt

Or manually:

pip install streamlit yfinance pandas numpy matplotlib seaborn scikit-learn ta

Step 3: Run the Application

streamlit run stock_prediction_app.py

---

## How It Works

1. User selects a stock and date range.
2. Historical data is fetched using yFinance.
3. Technical indicators (MA & RSI) are calculated.
4. Trading signal is generated.
5. Machine learning model is trained.
6. Next-day price prediction is displayed.
7. Interactive charts are rendered.

---

## Future Improvements

- LSTM Deep Learning model
- Multi-feature regression (Volume, RSI, MA)
- Candlestick charts
- Portfolio optimization engine
- Risk metrics (Sharpe Ratio, Beta, Alpha)
- Real-time auto-refresh
- Cloud deployment with CI/CD

---

## Disclaimer

This project is developed for educational and research purposes only.  
It does not provide financial advice.  
Stock market investments involve risk.

---

## Author

Aditya Bet  
Data Scientist | Machine Learning | Financial Analytics  

GitHub: https://github.com/adityabet  
LinkedIn: https://linkedin.com/in/aditya-bet-592372219  
