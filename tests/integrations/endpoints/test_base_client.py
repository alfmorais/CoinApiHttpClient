from coinapihttpclient.integrations.endpoints import CoinApiBaseClient

client = CoinApiBaseClient(
    base_url="www.example.com.br",
    token="example-jwt-token",
)


def test_base_client_parameters():
    expected_url = "www.example.com.br"
    expected_token = "example-jwt-token"

    assert client.base_url == expected_url
    assert client.token == expected_token


def test_base_client_headers_propert():
    expected_token = "example-jwt-token"
    expected_headers = {"X-CoinAPI-Key": expected_token}

    assert client.headers == expected_headers
