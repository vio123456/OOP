-- Assuming you're in the SQLite CLI connected to your database

-- Create tables
CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    price_per_kilo NUMERIC NOT NULL
);

CREATE TABLE IF NOT EXISTS receipt (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cashier TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS product_receipt (
    amount NUMERIC NOT NULL,
    product_id INTEGER,
    receipt_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (receipt_id) REFERENCES receipt(id)
);

-- Set mode for CSV import and import data
.mode csv
.headers on
.import --csv --skip 1 t4_product.csv product
.import --csv --skip 1 t4_receipt.csv receipt
.import --csv --skip 1 t4_product_receipt.csv product_receipt

-- Now, if you query the data, ensure .headers is set to on
.headers on
SELECT * FROM product_receipt;
