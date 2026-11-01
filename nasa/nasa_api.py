
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NASA_API_KEY")

BASE_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic/"


def fetch_apod(params=None):
    """Fetch astronomy data from NASA."""

    if params is None:
        params = {}

    params["api_key"] = API_KEY

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        # Normalize the response into a list
        if isinstance(data, dict):
            return [data]

        return data

    except requests.exceptions.RequestException as error:
        print("NASA API Error:", error)
        return []

    except ValueError:
        print("Invalid JSON response from NASA.")
        return []


def get_today_picture():
    """Get today's astronomy picture."""

    data = fetch_apod()

    return data[0] if data else None


def get_picture_by_date(date):
    """Get astronomy picture for a specific date."""

    data = fetch_apod({"date": date})

    return data[0] if data else None


def get_random_pictures(count=5):
    """Get random astronomy pictures."""

    if not 1 <= count <= 25:
        raise ValueError("Count must be between 1 and 25.")

    return fetch_apod({"count": count})
