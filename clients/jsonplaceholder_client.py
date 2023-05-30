import requests
from config import jsonplaceholder_url


class JSONPlaceHolderClient:
    def request_place_holder(self, path):
        response = requests.get(
            url=f'{jsonplaceholder_url}{path}',
        )
        return response
