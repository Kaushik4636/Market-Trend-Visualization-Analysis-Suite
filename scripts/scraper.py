import yfinance as ticker_data
import psycopg2
from datetime import datetime

# 1. DATABASE CREDENTIALS 
DB_CONFIG = {
    "host": "localhost",
    "database": "market_db",
    "user": "postgres",
    "password": "admin123" 
}

def fetch_and_push():
    conn = None
    try:
        # Connect to Postgres
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        assets = ['AAPL', 'TSLA', 'BTC-USD', 'ETH-USD']
        print(f"Fetching data at {datetime.now()}...")

        for sym in assets:
            # Fetch live data
            ticker = ticker_data.Ticker(sym)
            data = ticker.history(period='1d')
            
            if not data.empty:
                # CONVERSION STEP: .item() converts numpy.float64 to a standard Python float
                latest_price = float(data['Close'].iloc[-1]) 
                latest_vol = int(data['Volume'].iloc[-1])

                # Insert into PostgreSQL
                query = "INSERT INTO market_trends (symbol, price, volume) VALUES (%s, %s, %s)"
                cur.execute(query, (sym, latest_price, latest_vol))
            else:
                print(f"No data found for {sym}")
        
        conn.commit()
        print("✅ Successfully updated database with standard Python types!")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    fetch_and_push()