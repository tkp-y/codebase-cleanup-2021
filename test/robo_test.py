
from dotenv import load_dotenv
import os

from app.robo import request_data

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="abc123")

def test_request_data():
    valid_data = request_data("AAPL", API_KEY)
    assert list(valid_data.keys())[0] == "Meta Data"
    assert list(valid_data.keys())[1] == "Time Series (Daily)"
    assert valid_data["Meta Data"]["2. Symbol"] == "AAPL"


# TODO: test the code
