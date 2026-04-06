Market Trend Visualization & Analysis Suite
🎯 Project Overview
This project implements an automated end-to-end data pipeline to track and visualize financial market trends. It handles real-time data ingestion from financial APIs, stores structured data in a relational database, and provides a dynamic BI dashboard for stakeholder analysis.

🏗️ Architecture
Data Ingestion: Python script using yfinance to fetch live Ticker data (Stocks & Crypto).

Database: PostgreSQL relational database for persistent storage and historical trend tracking.

ETL Process: Python logic to handle data type conversion (NumPy to Native Python) and SQL injection.

Visualization: Power BI dashboard connected via PostgreSQL connector for real-time monitoring.

🛠️ Technical Stack
Language: Python 3.13

Database: PostgreSQL 16

Libraries: psycopg2 (Database Driver), yfinance (Financial Data), pandas (Data Handling)

BI Tool: Power BI Desktop

📂 Key Features
Automated Scraper: A modular Python script that handles API rate limits and data validation.

Relational Schema: Optimized SQL table structure with auto-incrementing IDs and localized timestamps.

Power BI Dashboard: Includes:

Price Volatility Trends: Multi-line charts comparing asset performance.

Volume Analysis: Clustered columns to identify high-liquidity periods.

Real-time Cards: Dynamic KPIs showing the latest price for AAPL, TSLA, BTC, and ETH.

🚀 How to Replicate
Database Setup: - Execute scripts/db_setup.sql in pgAdmin to create the market_trends table.

Python Environment:

Install dependencies: pip install psycopg2-binary yfinance pandas

Run python scripts/scraper.py to populate the database.

Visualization:

Open dashboards/market_analysis.pbix in Power BI.

Update the Data Source Settings to point to your local PostgreSQL instance.

💡 Business Impact
By automating the data collection process, this suite eliminates manual data entry and provides 100% accurate, minute-by-minute insights into market movements, enabling faster decision-making for portfolio adjustments.