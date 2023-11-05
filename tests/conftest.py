import pytest


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("X-CoinAPI-Key", "DUMMY")],
    }
