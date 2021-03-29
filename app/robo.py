
import os
import json
from dotenv import load_dotenv
import requests
from pandas import DataFrame
import plotly.express as px

from app.number_decorators import format_usd


def request_data(symbol_input, key):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol_input}&apikey={key}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return parsed_response


if __name__ == '__main__':

    load_dotenv()

    API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="abc123")

    # FETCH DATA

    symbol = input("Please input a stock symbol (e.g. 'MSFT'): ")
    new_parsed_response = request_data(symbol, API_KEY)

    # PROCESS DATA

    records = []
    for date, daily_data in new_parsed_response["Time Series (Daily)"].items():
        record = {
            "date": date,
            "open": float(daily_data["1. open"]),
            "high": float(daily_data["2. high"]),
            "low": float(daily_data["3. low"]),
            "close": float(daily_data["4. close"]),
            "volume": int(daily_data["5. volume"]),
        }
        records.append(record)

    df = DataFrame(records)

    # DISPLAY RESULTS

    print("LATEST CLOSING PRICE: ", format_usd(records[0]["close"]))
   # print("LATEST CLOSING PRICE: ", format_usd(df.iloc[0]["close"]))
    print("RECENT HIGH: ", format_usd(df["high"].max()))
    print("RECENT LOW: ", format_usd(df["low"].min()))

    # EXPORT PRICES TO CSV

    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", f"{symbol.lower()}_prices.csv")
    df.to_csv(csv_filepath)

    # CHART PRICES OVER TIME

    fig = px.line(df, y="close", title=f"Closing Prices for {symbol.upper()}") # see: https://plotly.com/python-api-reference/generated/plotly.express.line
    fig.show()
