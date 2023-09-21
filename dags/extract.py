import os

from airflow.models import Variable
from kaggle.api.kaggle_api_extended import KaggleApi


def prepare_env():
    """
    Prepares the environment for Kaggle API by setting up
    the required username and key from Airflow Variables.
    The username and key are retrieved from Airflow's Variable
    feature and stored in the environment variables, so the
    Kaggle API can access them for authentication.
    """
    os.environ["KAGGLE_USERNAME"] = Variable.get(
        "KAGGLE_USERNAME"
    )
    os.environ["KAGGLE_KEY"] = Variable.get("KAGGLE_KEY")


def extract_data():
    """
    Extracts data using the Kaggle API.
    This function prepares the environment, authenticates with Kaggle,
    and then downloads the specified dataset file to the specified path.

    Dataset: josephinelsy/spotify-top-hit-playlist-2010-2022
    File: playlist_2010to2022.csv
    Path: files/
    """
    prepare_env()

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_file(
        "josephinelsy/spotify-top-hit-playlist-2010-2022",
        file_name="playlist_2010to2022.csv",
        path="files/",
    )
