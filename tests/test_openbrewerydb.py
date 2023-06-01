import pytest
import requests

from config import openbrewerydb_url


class Test200:
    def test_response_id_equal_to_id(self, brewery_db):
        response = brewery_db.request_brewery_db(path="/", status_code=200)
        assert response != []

    @pytest.mark.parametrize("param", ["33139"])
    def test_response_has_value(self, brewery_db, param):
        response = brewery_db.request_brewery_db(path="/?by_postal"+param, status_code=200)
        assert response[0]['name'] != ['Abbey Brewing Co']

    @pytest.mark.parametrize("test_input, expected", [
        ('?by_type=micro&per_page=3', 'micro'),
        ('?by_type=brewpub&per_page=3', 'brewpub'),
        ('?by_type=regional&per_page=3', 'regional'),
    ])
    def test_message_error(self, brewery_db, test_input, expected):
        response = brewery_db.request_brewery_db(path=test_input, status_code=200)
        assert response[0]['brewery_type'] == expected


class Test40x:
    @pytest.mark.parametrize("method, status", [('post', 404), ('get', 200), ('put', 404), ('delete', 404)])
    def test_methods_for_brewery_api(self, place_holder, method, status):
        request = getattr(requests, method)
        response = request(openbrewerydb_url)
        assert response.status_code == status

    def test_message_error(self, brewery_db):
        response = brewery_db.request_brewery_db(path="/sds", status_code=404)
        assert response['message'] == "Couldn't find Brewery"
