import pytest
import requests

from config import jsonplaceholder_url


class Test200:
    def test_response_not_empty(self, place_holder):
        response = place_holder.request_place_holder(path="?per_page=1", status_code=200)
        assert response != []

    @pytest.mark.parametrize("test_input, expected", [
        ('/1', 1),
        ('/10', 10),
    ])
    def test_brewery_id(self, place_holder, test_input, expected):
        response = place_holder.request_place_holder(path=test_input, status_code=200)
        assert response['id'] == expected

    @pytest.mark.parametrize("test_input, expected", [
        ('/1', 'delectus aut autem'),
        ('/10', 'illo est ratione doloremque quia maiores aut'),
    ])
    def test_title(self, place_holder, test_input, expected):
        response = place_holder.request_place_holder(path=test_input, status_code=200)
        assert response['title'] == expected


class Test40x:
    def test_message_error(self, place_holder):
        response = place_holder.request_place_holder(path="/sds", status_code=404)
        assert response == {}

    @pytest.mark.parametrize("method, status", [('post', 201), ('get', 200), ('put', 404), ('delete', 404)])
    def test_methods_for_brewery_api(self, place_holder, method, status):
        request = getattr(requests, method)
        response = request(jsonplaceholder_url)
        assert response.status_code == status
