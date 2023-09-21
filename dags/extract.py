from kaggle.api.kaggle_api_extended import KaggleApi
from airflow.models import Variable
import os


def prepare_env():
    os.environ["KAGGLE_USERNAME"] = Variable.get("KAGGLE_USERNAME")
    os.environ["KAGGLE_KEY"] = Variable.get("KAGGLE_KEY")


def extract_data():
    prepare_env()

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_file(
        "josephinelsy/spotify-top-hit-playlist-2010-2022",
        file_name="playlist_2010to2022.csv",
        path="files/",
    )
