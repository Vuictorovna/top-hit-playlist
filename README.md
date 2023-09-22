# Spotify Data Pipeline with Airflow

## Objective

This project focuses on constructing a robust data pipeline using Apache Airflow to orchestrate Extract, Transform, Load (ETL) workflows. The pipeline ingests Spotify Top Hit playlists data from 2010 to 2022, processes it to glean insights into trends and preferences in popular songs and loads the transformed data into an SQLite database for further analysis.

## Features

- **Data Extraction**: Efficiently downloads Spotify playlist data from Kaggle.
- **Data Transformation**: Cleans and transforms raw data, handling missing values, deduplication, and feature engineering.
- **Data Loading**: Stores the cleaned and transformed data into an SQLite database.
- **Scheduling and Monitoring**: Utilizes Airflow to schedule and monitor the workflow execution.

## Technologies Used

### Apache Airflow

A platform to programmatically author, schedule, and monitor workflows.

- [Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html)

### SQLite

A C library that provides a lightweight, disk-based database.

- [SQLite Documentation](https://www.sqlite.org/docs.html)

### Pandas

A fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation tool, built on top of the Python programming language.

- [Pandas Documentation](https://pandas.pydata.org/docs/)

### Python

The project is implemented in Python, leveraging its extensive libraries and tools.

- [Python Official Website](https://www.python.org)

## Setup

### Prerequisites

1. Python 3.7 or above
2. Apache Airflow 2.2 or above
3. Pip

### Installation

1. Clone the repository.

   ```bash
   git clone https://github.com/Vuictorovna/top-hit-playlist.git
   ```

2. Navigate into the directory.

   ```bash
   cd top-hit-playlist
   ```

3. Setting Up a Virtual Environment.

   To isolate the project dependencies, it's recommended to create a virtual environment.
   Run the following commands in your terminal to create and activate a virtual environment:

   **On macOS and Linux:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   **On Windows:**

   ```bash
   python -m venv venv
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\venv\Scripts\activate
   ```

4. Install the required packages.

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Create the necessary environment variables for Kaggle API credentials in Airflow:

- Navigate to the Airflow web interface, go to Admin -> Variables.
- Add KAGGLE_USERNAME and KAGGLE_KEY with your Kaggle API credentials.

## Usage

1. **Start the Airflow web server (in one terminal window):**

   ```bash
   airflow webserver -p 8080
   ```

2. **Start the Airflow scheduler (in another terminal window):**

   ```bash
   airflow scheduler
   ```

3. **Navigate to the Airflow UI at http://localhost:8080 and trigger the data_pipeline_dag to run the workflow.**

4. **You can monitor the progress, check logs, and analyze the DAG execution in the Airflow UI.**
