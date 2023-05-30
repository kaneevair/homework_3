import pytest
from hamcrest import assert_that, equal_to, is_not


class Test200:
    @pytest.mark.parametrize("param, expected", [
        ("/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0", "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0")
    ])
    def test_response_id_equal_to_id(self, brewery_db, param, expected):
        response = brewery_db.request_brewery_db(path=param).json()
        assert_that(
                    actual=response['id'],
                    matcher=equal_to(expected)
                )

    @pytest.mark.parametrize("param", ["/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"])
    def test_response_has_value(self, brewery_db, param):
        response = brewery_db.request_brewery_db(path=param).json()
        assert_that(
            actual=response['name'] and response['website_url'],
            matcher=is_not('')
        )

    @pytest.mark.parametrize("test_input, expected", [
        ('?by_type=micro&per_page=3', 'micro'),
        ('?by_type=brewpub&per_page=3', 'brewpub'),
        ('?by_type=regional&per_page=3', 'regional'),
    ])
    def test_message_error(self, brewery_db, test_input, expected):
        response = brewery_db.request_brewery_db(path=test_input).json()
        assert response[0]['brewery_type'] == expected


class Test40x:
    def test_code_error(self, brewery_db):
        response = brewery_db.request_brewery_db(path="/sds")
        assert response.status_code == 404

    def test_message_error(self, brewery_db):
        response = brewery_db.request_brewery_db(path="/sds").json()
        assert response['message'] == "Couldn't find Brewery"
