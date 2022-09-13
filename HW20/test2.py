import json

import pytest

import pytz
from datetime import datetime
from datetime import timedelta

from requests import post
from config import ConfigBaseUrl
from config import ConfigHeaders
from config import ConfigPhotoUrl


@pytest.fixture(scope="module", autouse=True)
def url_scope():
    ConfigBaseUrl.base_url = "https://petstore.swagger.io/v2/pet"


@pytest.fixture(scope="module", autouse=True)
def photo_scope():
    ConfigBaseUrl.base_url = "https://www.shutterstock.com/" \
                             "image-photo/" \
                             "funny-dog-licking-lips-tongue-out-1761385949"


@pytest.fixture(scope="function", autouse=True)
def header_scope():
    # My time was different from the server time, so I use subtracting one second
    date_now = datetime.now(tz=pytz.timezone('UTC')) + timedelta(seconds=1)
    date_str = date_now.strftime("%a, %d %b %Y %T GMT")
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


@pytest.fixture(scope='function', autouse=True)
def json_scope():
    def json_wrapper(*args):
        print(len(args))
        json_body = json.dumps(
            {
                "id": 0,
                "category":
                    {
                        "id": 0,
                        "name": f"{args[2]}"
                    },
                "name": f"{args[3]}",
                "photoUrls":
                    [
                        f"{args[4]}"
                    ],
                "tags":
                    [
                        {
                            "id": 0,
                            "name": f"{args[5]}"
                        }
                    ],
                "status": f"{args[1]}"
            }
        )

        return json_body

    return json_wrapper


@pytest.mark.parametrize(["json_scope", "status", "name1", "name2", "photo", "name3"],
                         [["json_scope", "available", "Bob", "doggie", ConfigPhotoUrl.photo, "Williams"],
                          ["json_scope", "pending", "Billy", "doggie", ConfigPhotoUrl.photo, "Robert"],
                          ["json_scope", "sold", "Marta", "doggie", ConfigPhotoUrl.photo, "Jack"]],
                         indirect=["json_scope"])
def test_pet_post1(json_scope, status, name1, name2, photo, name3):
    fixture_execute = json_scope(json_scope, status, name1, name2, photo, name3)
    test_request = post(ConfigBaseUrl.base_url, json=fixture_execute)

    assert test_request.status_code == 405


@pytest.mark.parametrize(["json_scope", "status", "name1", "name2", "photo", "name3"],
                         [["json_scope", "available", "Bob", "doggie", ConfigPhotoUrl.photo, "Williams"],
                          ["json_scope", "pending", "Billy", "doggie", ConfigPhotoUrl.photo, "Robert"],
                          ["json_scope", "sold", "Marta", "doggie", ConfigPhotoUrl.photo, "Jack"]],
                         indirect=["json_scope"])
def test_pet_post2(json_scope, status, name1, name2, photo, name3):
    fixture_execute = json_scope(json_scope, status, name1, name2, photo, name3)
    test_request = post(ConfigBaseUrl.base_url, json=fixture_execute)

    assert test_request.headers == ConfigHeaders.headers


@pytest.mark.parametrize(["json_scope", "status", "name1", "name2", "photo", "name3"],
                         [["json_scope", "available", "Bob", "doggie", ConfigPhotoUrl.photo, "Williams"],
                          ["json_scope", "pending", "Billy", "doggie", ConfigPhotoUrl.photo, "Robert"],
                          ["json_scope", "sold", "Marta", "doggie", ConfigPhotoUrl.photo, "Jack"]],
                         indirect=["json_scope"])
def test_pet_post3(json_scope, status, name1, name2, photo, name3):
    fixture_execute = json_scope(json_scope, status, name1, name2, photo, name3)
    test_request = post(ConfigBaseUrl.base_url, json=fixture_execute)
    test_output = 'Invalid input'

    assert test_output in str(test_request.content)
