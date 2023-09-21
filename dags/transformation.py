import pandas as pd


def transform_data():
    df = pd.read_csv("files/playlist_2010to2022.csv")
    df = df.dropna()
    df["duration_mins"] = (df["duration_ms"] / (1000 * 60)).round(2)
    df.drop_duplicates(inplace=True)
    df["track_name"] = df["track_name"].str.lower().str.replace("[^a-z0-9 ]", "")

    df.to_csv("files/clean_data.csv", index=False)
