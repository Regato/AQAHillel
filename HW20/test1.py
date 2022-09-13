import json

import pytest

import pytz
from datetime import datetime
from datetime import timedelta

from requests import get
from config import ConfigBaseUrl
from config import ConfigHeaders


@pytest.fixture(scope="module", autouse=True)
def url_scope():
    ConfigBaseUrl.base_url = 'https://petstore.swagger.io/v2/pet/findByStatus'


@pytest.fixture(scope="function", autouse=True)
def header_scope():
    # My time was different from the server time, so I use subtracting one second
    date_now = datetime.now(tz=pytz.timezone('UTC')) + timedelta(seconds=1)
    date_str = date_now.strftime('%a, %d %b %Y %T GMT')
    ConfigHeaders.headers = json.dumps({
        'Date': f'{date_str}',
        'Content-Type': 'application/json',
        'Transfer-Encoding': 'chunked',
        'Connection': 'keep-alive',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, DELETE, PUT',
        'Access-Control-Allow-Headers': 'Content-Type, '
                                        'api_key, '
                                        'Authorization',
        'Server': 'Jetty(9.2.9.v20150224)'
    })


@pytest.mark.parametrize('query',
                         [{"status": ["available"]},
                          {"status": ["pending"]},
                          {"status": ["sold"]}])
def test_find_status1(query):
    test_request = get(ConfigBaseUrl.base_url, params=query)

    assert test_request.status_code == 200


@pytest.mark.parametrize('query',
                         [{"status": ["available"]},
                          {"status": ["pending"]},
                          {"status": ["sold"]}])
def test_find_status2(query):
    test_request = get(ConfigBaseUrl.base_url, params=query)

    assert test_request.headers == ConfigHeaders.headers


@pytest.mark.parametrize('query',
                         [{"status": ["available"]},
                          {"status": ["pending"]},
                          {"status": ["sold"]}])
def test_find_status3(query):
    test_request = get(ConfigBaseUrl.base_url, params=query)

    assert test_request.json()[1]["status"] == query["status"][0]


@pytest.mark.parametrize('query',
                         [{"status": ["good"]},
                          {"status": ["bad"]},
                          {"status": ["nice"]}])
def test_find_status4(query):
    test_request = get(ConfigBaseUrl.base_url, params=query)

    assert test_request.status_code == 400


@pytest.mark.parametrize('query',
                         [{"status": ["good"]},
                          {"status": ["bad"]},
                          {"status": ["nice"]}])
def test_find_status5(query):
    test_request = get(ConfigBaseUrl.base_url, params=query)

    assert test_request.headers == ConfigHeaders.headers


@pytest.mark.parametrize('query',
                         [{"status": ["good"]},
                          {"status": ["bad"]},
                          {"status": ["nice"]}])
def test_find_status6(query):
    test_request = get(ConfigBaseUrl.base_url, params=query)

    assert test_request.json() == []
