import requests
from config import openbrewerydb_url


class OpenBreweryDBClient:
    @staticmethod
    def request_brewery_db(path, status_code) -> dict:
        response = requests.get(
            url=f'{openbrewerydb_url}{path}',
        )
        assert response.status_code == status_code
        return response.json()
