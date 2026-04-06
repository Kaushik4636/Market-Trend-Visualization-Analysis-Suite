CREATE TABLE market_trends (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10),
    price DECIMAL(10, 2),
    volume BIGINT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);