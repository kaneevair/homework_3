import requests
from config import openbrewerydb_url


class OpenBreweryDBClient:
    def request_brewery_db(self, path):
        response = requests.get(
            url=f'{openbrewerydb_url}{path}',
        )
        return response
