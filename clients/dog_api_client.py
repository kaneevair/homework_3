import requests
from config import dog_api_url

class DogApiClient:
    @staticmethod
    def request_dog_api(path, status_code) -> dict:
        response = requests.get(
            url=f'{dog_api_url}{path}',
        )
        assert response.status_code == status_code
        return response.json()
