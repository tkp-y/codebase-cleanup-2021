
from dotenv import load_dotenv
import os
import pytest
from pandas import DataFrame
import pandas as pd

from app.robo import request_data

load_dotenv()

API_KEY = os.getenv("CI_ALPHAVANTAGE_API_KEY", default="abc123")

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server") # skips this test on CI
def test_request_data():
    valid_data = request_data("AAPL", API_KEY)
    assert list(valid_data.keys())[0] == "Meta Data"
    assert list(valid_data.keys())[1] == "Time Series (Daily)"
    assert valid_data["Meta Data"]["2. Symbol"] == "AAPL"

@pytest.fixture(scope="module")
def mock_robo_data():
    data = open('test/mock_data/mock_robo_data.txt', 'r')

def test_convert_data(mock_robo_data):
    test_parsed_response = mock_robo_data
    expected_data = [

        [
            "2021-03-29",
            "121.6500",
            "122.5800",
            "120.7300",
            "121.3900",
            "80543668"
        ],
        [
            "2021-03-26",
            "120.3500",
            "121.4800",
            "118.9200",
            "121.2100",
             "94071234"
        ]
    ]
    expected_response =  pd.DataFrame(expected_data, index = ["date", "open", "high", "low", "close", "volume"])

    result_df = convert_data(test_parsed_response)
    assert expected_response == result_df







