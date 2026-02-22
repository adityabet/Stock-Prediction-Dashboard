# 🚀📈 AI-Powered Stock Market Prediction Dashboard  

> 💡 Real-Time Stock Analysis + 📊 Technical Indicators + 🤖 Machine Learning Forecasting  

---

## 🌟 Project Overview

The **Stock Market Prediction Dashboard** is an interactive financial analytics web app built using **Python & Streamlit**.

It combines:

✨ Technical Analysis  
📊 Performance Analytics  
📉 Trend Detection  
🤖 Machine Learning Prediction  
💹 Real-Time Market Data  

This project demonstrates strong understanding of:

- 📈 Financial Data Engineering  
- 🧠 Supervised Learning  
- 📊 Time-Series Analysis  
- 🖥 Interactive Dashboard Development  

---

## 🔥 Key Features

### 🏢 1️⃣ Multi-Stock Support

Supports both US 🇺🇸 and Indian 🇮🇳 stocks:

- 🍎 Apple (AAPL)
- 🚗 Tesla (TSLA)
- 🖥 Microsoft (MSFT)
- 🌐 Google (GOOGL)
- 📦 Amazon (AMZN)
- 🏦 TCS (India)
- 🛢 Reliance (India)

---

### 📊 2️⃣ Technical Indicators

#### 📈 Moving Averages
- 100-Day Moving Average
- 200-Day Moving Average
- 🟢 Golden Cross Detection
- 🔴 Death Cross Detection

#### 📉 RSI (Relative Strength Index)
- Period: 14
- 🔴 Overbought Level: 70
- 🟢 Oversold Level: 30
- ⚡ Momentum Reversal Insights

---

### 🎯 3️⃣ Smart Trading Signal Engine

Signal Logic:

BUY  → MA100 > MA200 AND RSI < 70  
SELL → MA100 < MA200 AND RSI > 30  
HOLD → Otherwise  

Output:

🟢 BUY  
🔴 SELL  
🟡 HOLD  

Displayed instantly as the **Current Recommendation**.

---

### 📆 4️⃣ Performance Analytics

📊 Yearly Average Return  
🏆 Highest Daily Return  
📅 Best Performing Day  
📈 Historical Data Table  
⚡ Volatility Insight  

---

### 🤖 5️⃣ Machine Learning Prediction

Model Used:
- Linear Regression
- Time-Series Based Train/Test Split (80/20)
- 📏 R² Score Evaluation

Outputs:
- 📊 Model Accuracy
- 🔮 Predicted Next-Day Price
- 📉 Actual vs Predicted Graph

Demonstrates:

🧠 Supervised Learning  
📊 Model Evaluation  
⚙ Feature Engineering  
📈 Forecasting Techniques  

---

## 🛠 Tech Stack

### 👨‍💻 Backend & ML
- 🐍 Python
- 🤖 Scikit-Learn
- 🧮 NumPy
- 🗂 Pandas

### 📊 Visualization
- 📉 Matplotlib
- 🎨 Seaborn

### 📡 Data Source
- 📈 yFinance

### 🖥 Frontend
- ⚡ Streamlit

---

## 📂 Project Structure

Stock_Prediction_App/  
│  
├── stock_prediction_app.py  
├── requirements.txt  
└── README.md  

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

git clone https://github.com/your-username/stock-prediction-dashboard.git  
cd stock-prediction-dashboard  

---

### 2️⃣ Install Dependencies

pip install -r requirements.txt  

Or manually:

pip install streamlit yfinance pandas numpy matplotlib seaborn scikit-learn ta  

---

### 3️⃣ Run Application

streamlit run stock_prediction_app.py  

---

## 🧠 How It Works

1️⃣ Select Stock & Date Range  
2️⃣ Fetch Historical Data (yFinance)  
3️⃣ Calculate Technical Indicators  
4️⃣ Generate Trading Signal  
5️⃣ Train ML Model  
6️⃣ Predict Next-Day Price  
7️⃣ Display Interactive Visual Dashboard  

---

## 🔮 Future Improvements

🚀 LSTM Deep Learning Model  
📊 Multi-Factor Regression  
🕯 Candlestick Charts  
💼 Portfolio Optimization  
📉 Risk Metrics (Sharpe Ratio, Beta, Alpha)  
☁ Cloud Deployment  
🔄 Real-Time Auto Refresh  

---

## ⚠ Disclaimer

📌 This project is for educational purposes only.  
💰 It does not provide financial advice.  
📉 Stock markets involve risk.

---

## 👨‍💻 Author

**Aditya Bet**  
📊 Data Scientist | 🤖 Machine Learning | 📈 Financial Analytics  

🔗 GitHub: https://github.com/adityabet  
🔗 LinkedIn: https://linkedin.com/in/aditya-bet-592372219  

---

⭐ If you found this project useful, consider giving it a star!
