# 📊 Market Trend Visualization & Analysis Suite

## 🎯 Project Overview
Designed and implemented an end-to-end data pipeline to ingest, store, and visualize near real-time financial market data. The system automates data collection from external APIs, persists it in a relational database, and delivers actionable insights through an interactive BI dashboard.

---

## 🏗️ Architecture

### 🔹 Data Ingestion
Python-based pipeline using `yfinance` to fetch stock and cryptocurrency data.

### 🔹 Database Layer
PostgreSQL is used for structured storage, enabling efficient querying and historical tracking.

### 🔹 ETL Processing
Custom Python scripts handle:
- Data cleaning and validation  
- Conversion of NumPy/Pandas types to native Python types  
- Safe database insertion using parameterized queries (`psycopg2`)  

### 🔹 Visualization Layer
Interactive dashboard built in Power BI connected directly to PostgreSQL.

---

## 🛠️ Technical Stack

- **Language:** Python 3.13  
- **Database:** PostgreSQL 16  
- **Libraries:** pandas, yfinance, psycopg2  
- **BI Tool:** Power BI Desktop  

---

## 📂 Key Features

- ✅ Automated data pipeline with error handling  
- ✅ Optimized relational schema for time-series data  
- ✅ Real-time dashboard with financial insights  

### 📊 Dashboard Includes:
- Price trend comparison (multi-line charts)  
- Volume analysis (clustered columns)  
- KPI cards for AAPL, TSLA, BTC, ETH  

---

## 🚀 How to Replicate

### 1️⃣ Database Setup

Run the following SQL in pgAdmin:

```sql
CREATE TABLE market_trends (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10),
    price DECIMAL(10, 2),
    volume BIGINT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
