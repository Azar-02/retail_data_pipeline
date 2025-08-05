import pandas as pd
import sqlite3

def save_to_csv(df, path):
    df.to_csv(path, index=False)

def save_to_sqlite(df, db_path):
    conn = sqlite3.connect(db_path)
    df.to_sql('retail_summary', conn, if_exists='replace', index=False)
    conn.close()
