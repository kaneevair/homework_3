import pytest
import requests


def url_ya(parser):
    parser.addoption(
        "--base_url", default="https://ya.ru", help="This is request url"
    )

    parser.addoption(
        "--status_code", type=int, default=200, help="This is response status code"
    )


@pytest.fixture(scope="session")
def base_url(request):
    base_url = request.config.getoption("--base_url")
    return base_url


@pytest.fixture(scope="session")
def status_code(request):
    status = request.config.getoption("--status_code")
    return status


def test_url_status(base_url, status_code):
    response = requests.get(base_url)
    assert response.status_code == status_code
