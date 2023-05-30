import pytest
from hamcrest import assert_that, has_string, is_not


class Test200:
    def test_response_not_empty(self, dog_api):
        response = dog_api.request_dog_api(path="/random").json()
        assert_that(
                    actual=response,
                    matcher=is_not({})
                )

    def test_status_success(self, dog_api):
        response = dog_api.request_dog_api(path="/random").json()
        assert_that(
            actual=response['status'],
            matcher=has_string('success')
        )

    def test_message_not_empty(self, dog_api):
        response = dog_api.request_dog_api(path="/random").json()
        assert_that(
                    actual=response['message'],
                    matcher=is_not('')
                )


class Test40x:
    @pytest.mark.parametrize("param", ["/sds"])
    def test_status_error(self, dog_api, param):
        response = dog_api.request_dog_api(path=param).json()
        assert_that(
            actual=response['status'],
            matcher=has_string('error')
        )

    def test_code_error(self, dog_api):
        response = dog_api.request_dog_api(path="/sds").json()
        assert_that(
            actual=response['code'],
            matcher=has_string('404')
        )

    @pytest.mark.parametrize("test_input, expected", [
        ('/sds', 'No route found for \"GET http://dog.ceo/api/breeds/image/sds" with code: 0'),
        ('/randomm', 'No route found for \"GET http://dog.ceo/api/breeds/image/randomm" with code: 0'),
    ])
    def test_message_error(self, dog_api, test_input, expected):
        response = dog_api.request_dog_api(path=test_input).json()
        assert_that(
            actual=response['message'],
            matcher=has_string(expected)
        )

