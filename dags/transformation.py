import pandas as pd


def transform_data():
    df = pd.read_csv("files/playlist_2010to2022.csv")
    df = df.dropna()  # Remove missing values
    df.to_csv("files/clean_data.csv", index=False)
