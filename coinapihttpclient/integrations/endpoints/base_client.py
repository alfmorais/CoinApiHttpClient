from coinapihttpclient.project.app import BASE_URL, TOKEN


class CoinApiBaseClient:
    def __init__(self, base_url: str = BASE_URL, token: str = TOKEN) -> None:
        self.base_url = base_url
        self.token = token

    @property
    def headers(self) -> dict:
        return {"X-CoinAPI-Key": self.token}
