import pytest
from hamcrest import assert_that, is_not


class Test200:
    def test_response_not_empty(self, place_holder):
        response = place_holder.request_place_holder(path="?per_page=1").json()
        assert_that(
                    actual=response,
                    matcher=is_not({})
                )

    @pytest.mark.parametrize("test_input, expected", [
        ('/1', 1),
        ('/10', 10),
    ])
    def test_message_error(self, place_holder, test_input, expected):
        response = place_holder.request_place_holder(path=test_input).json()
        assert response['id'] == expected

    @pytest.mark.parametrize("test_input, expected", [
        ('/1', 'delectus aut autem'),
        ('/10', 'illo est ratione doloremque quia maiores aut'),
    ])
    def test_message_error(self, place_holder, test_input, expected):
        response = place_holder.request_place_holder(path=test_input).json()
        assert response['title'] == expected


class Test40x:
    def test_code_error(self, place_holder):
        response = place_holder.request_place_holder(path="/sds")
        assert response.status_code == 404

    def test_message_error(self, place_holder):
        response = place_holder.request_place_holder(path="/sds").json()
        assert response == {}
