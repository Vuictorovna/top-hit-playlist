import sqlite3

import pandas as pd


def load_data():
    """
    Loads the transformed data into a SQLite database.

    The function performs the following steps:
    - Connects to the SQLite database.
    - Reads the cleaned dataset from the CSV file.
    - Loads the DataFrame into a new SQL table, 'table_name', in the connected database.
    - If 'table_name' already exists in the database, it replaces the existing table.
    - Doesn’t write row names (index) into the SQL table.
    """
    conn = sqlite3.connect("files/data.db")
    df = pd.read_csv("files/clean_data.csv")
    df.to_sql(
        "table_name", conn, if_exists="replace", index=False
    )
