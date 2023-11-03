from collections.abc import Coroutine

import aiohttp

from .base_client import CoinApiBaseClient


class ListAllAssetsById(CoinApiBaseClient):
    async def handle(self, asset_id: str) -> Coroutine:
        endpoint = "v1/assets/{0}".format(asset_id)
        url = "{0}{1}".format(self.base_url, endpoint)

        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, headers=self.headers) as response:
                return await response.json(), response.status
