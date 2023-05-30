import pytest
import requests


def url_ya(parser):
    parser.addoption(
        "--base_url", action="store", default="https://ya.ru", help="help"
    )

    parser.addoption(
        "--status_code", action="store", default="200", help="help"
    )


@pytest.fixture
def base_url1(request):
    base_url = request.config.getoption("--base_url")
    return base_url


@pytest.fixture
def status_code1(request):
    status = request.config.getoption("--status_code")
    return status


def test_response_200ok(base_url1, status_code1):
    response = requests.get(base_url1)
    if response.url == base_url1:
        assert response.status_code == 200
    else:
        assert response.status_code == 404

