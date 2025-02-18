
from dotenv import load_dotenv
import os
import pytest


from app.robo import request_data
from app.number_decorators import format_usd

load_dotenv()

API_KEY = os.getenv("CI_ALPHAVANTAGE_API_KEY", default="abc123")

CI_ENV = os.getenv("CI") == "true"

#Test ability to request for a given stock symbol

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server") # skips this test on CI
def test_request_data():
    valid_data = request_data("AAPL", API_KEY)
    assert list(valid_data.keys())[0] == "Meta Data"
    assert list(valid_data.keys())[1] == "Time Series (Daily)"
    assert valid_data["Meta Data"]["2. Symbol"] == "AAPL"










