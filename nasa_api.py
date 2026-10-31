import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NASA_API_KEY")

BASE_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"


def get_astronomy_picture():

    params = {
        "api_key": API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    print("Status:", response.status_code)

    if response.status_code == 200:
        return response.json()

    else:
        print("Error details:", response.text)
        return None