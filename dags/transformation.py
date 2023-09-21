import pandas as pd


def transform_data():
    """
    Transforms the raw Spotify playlist data for further analysis.

    The function performs the following transformations:
    - Reads the dataset from the CSV file.
    - Drops rows with any missing values.
    - Converts song duration from milliseconds to minutes and rounds it to two decimal places.
    - Removes duplicate rows based on all columns.
    - Normalizes the 'track_name' by converting it to lower case and removing any character that is not a lower case letter, a digit, or a space.
    - Writes the transformed dataset back to a new CSV file.
    """
    df = pd.read_csv("files/playlist_2010to2022.csv")
    df = df.dropna()
    df["duration_mins"] = (
        df["duration_ms"] / (1000 * 60)
    ).round(2)
    df.drop_duplicates(inplace=True)
    df["track_name"] = (
        df["track_name"]
        .str.lower()
        .str.replace("[^a-z0-9 ]", "")
    )

    df.to_csv("files/clean_data.csv", index=False)
