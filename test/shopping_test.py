
#import the code we want to test
import os
import pytest
from pandas import read_csv

from app.shopping import format_usd, find_product

def test_format_usd():
    assert format_usd(9.5) == "$9.50"


@pytest.fixture(scope="module")
def mock_products():
    mock_products_filepath = os.path.join(os.path.dirname(__file__), "mock_data", "mock_products.csv")
    mock_products_df = read_csv(mock_products_filepath)
    return mock_products_df.to_dict("records")


def test_find_product(mock_products):
    # with valid product id, returns the product info:
    valid_result = find_product("8", mock_products)
    assert valid_result == {
        'aisle': 'Aisle C',
        'department': 'snacks',
        'id': 8,
        'name': 'Product 8',
        'price': 10.0
    }
    # with invalid product id, returns None:
    invalid_result = find_product("88888888", mock_products)
    assert invalid_result == None


