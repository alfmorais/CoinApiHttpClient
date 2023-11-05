import asyncio
from collections.abc import Coroutine

import pytest

from coinapihttpclient.integrations.endpoints import ListAllAssetsById


@pytest.mark.vcr()
def test_list_all_assets_by_id_success():
    expected_sorted_keys = [
        "asset_id",
        "data_end",
        "data_orderbook_end",
        "data_orderbook_start",
        "data_quote_end",
        "data_quote_start",
        "data_start",
        "data_symbols_count",
        "data_trade_end",
        "data_trade_start",
        "id_icon",
        "name",
        "price_usd",
        "type_is_crypto",
        "volume_1day_usd",
        "volume_1hrs_usd",
        "volume_1mth_usd",
    ]

    client = ListAllAssetsById()
    response = client.handle(asset_id="BTC")
    response_json = asyncio.run(response)

    assert isinstance(response, Coroutine)
    assert sorted(response_json[0][0].keys()) == expected_sorted_keys
    assert response_json[1] == 200


@pytest.mark.vcr()
def test_list_all_assets_by_id_error():
    client = ListAllAssetsById()
    response = client.handle(asset_id="some-asset-id")
    response_json = asyncio.run(response)

    assert isinstance(response, Coroutine)
    assert response_json[0] == []
    assert response_json[1] == 200
