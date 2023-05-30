import pytest

from clients.dog_api_client import DogApiClient
from clients.jsonplaceholder_client import JSONPlaceHolderClient
from clients.openbrewerydb_client import OpenBreweryDBClient


@pytest.fixture(scope='function')
def dog_api():
    return DogApiClient()


@pytest.fixture(scope='function')
def place_holder():
    return JSONPlaceHolderClient()


@pytest.fixture(scope='function')
def brewery_db():
    return OpenBreweryDBClient()


