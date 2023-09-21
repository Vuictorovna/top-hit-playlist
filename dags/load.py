import sqlite3
import pandas as pd


def load_data():
    conn = sqlite3.connect("files/data.db")
    df = pd.read_csv("files/clean_data.csv")
    df.to_sql("table_name", conn, if_exists="replace", index=False)
