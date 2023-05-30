import requests
from config import dog_api_url

class DogApiClient:
    def request_dog_api(self, path):
        response = requests.get(
            url=f'{dog_api_url}{path}',
        )
        return response
