import requests
from config import jsonplaceholder_url


class JSONPlaceHolderClient:
    @staticmethod
    def request_place_holder(path, status_code) -> dict:
        response = requests.get(
            url=f'{jsonplaceholder_url}{path}',
        )
        assert response.status_code == status_code
        return response.json()
