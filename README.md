📊 Market Trend Visualization & Analysis Suite
🎯 Project Overview

Designed and implemented an end-to-end data pipeline to ingest, store, and visualize real-time financial market data. The system automates data collection from external APIs, persists it in a relational database, and delivers actionable insights through an interactive BI dashboard.

🏗️ Architecture
Data Ingestion
Python-based pipeline using yfinance to fetch real-time stock and cryptocurrency data.
Database Layer
PostgreSQL used for structured storage, ensuring efficient querying and historical tracking.
ETL Processing
Custom Python scripts handle:
Data cleaning and validation
Conversion of NumPy/Pandas types to native Python types
Safe database insertion using parameterized queries (via psycopg2)
Visualization Layer
Interactive dashboard built in Microsoft Power BI connected directly to PostgreSQL.
🛠️ Technical Stack
Language: Python 3.13
Database: PostgreSQL 16
Libraries: pandas, yfinance, psycopg2
BI Tool: Power BI Desktop
📂 Key Features
Automated Data Pipeline
Modular scraper with error handling and API rate-limit awareness.
Optimized Relational Schema
Auto-incrementing primary keys
Timestamp-based tracking
Efficient storage for time-series data
Interactive Dashboard
📈 Price trend comparison (multi-line charts)
📊 Volume analysis (clustered columns)
⚡ Real-time KPI cards (AAPL, TSLA, BTC, ETH)
🚀 How to Replicate
1. Database Setup

Run your SQL script in pgAdmin:

CREATE TABLE market_trends (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10),
    price DECIMAL(10, 2),
    volume BIGINT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
2. Python Environment

Install dependencies:

pip install psycopg2-binary yfinance pandas

Run the scraper:

python scripts/scraper.py
3. Visualization
Open .pbix file in Power BI
Update PostgreSQL connection:
Server: localhost
Database: market_db
Username: postgres
Password: your password
💡 Business Impact
Eliminates manual data collection
Enables near real-time market monitoring
Supports data-driven decision-making for trading and portfolio analysis
