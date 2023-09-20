# Extraction function
import requests


def extract_data():
    url = "https://www.kaggle.com/datasets/josephinelsy/spotify-top-hit-playlist-2010-2022/download?datasetVersionNumber=1"
    response = requests.get(url)
    with open("files/raw_data.csv", "wb") as f:
        f.write(response.content)


# extract_data()
