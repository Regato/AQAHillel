import json

import pytest

import pytz
from datetime import datetime
from datetime import timedelta

from requests import put
from config import ConfigBaseUrl
from config import ConfigHeaders


@pytest.fixture(scope="module", autouse=True)
def url_scope():
    ConfigBaseUrl.base_url = "https://petstore.swagger.io/v2/pet"


@pytest.fixture(scope="function", autouse=True)
def header_scope():
    # My time was different from the server time, so I use subtracting one second
    date_now = datetime.now(tz=pytz.timezone('UTC')) + timedelta(seconds=1)
    date_str = date_now.strftime("%a, %d %b %Y %T GMT")
    ConfigHeaders.headers = json.dumps(
        {
            'Date': f'{date_str}',
            'Content-Type': 'application/json',
            'Transfer-Encoding': 'chunked',
            'Connection': 'keep-alive',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, DELETE, PUT',
            'Access-Control-Allow-Headers': 'Content-Type, api_key, Authorization',
            'Server': 'Jetty(9.2.9.v20150224)'
        }
    )


@pytest.fixture(scope='function', autouse=True)
def json_scope():
    def json_wrapper(*args):
        print(len(args))
        json_body = json.dumps(
            {
                "id": args[6],
                "category":
                    {
                        "id": args[7],
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
                            "id": args[8],
                            "name": f"{args[5]}"
                        }
                    ],
                "status": f"{args[1]}"
            }
        )

        return json_body

    return json_wrapper


@pytest.mark.parametrize(["json_scope", "status", "name1", "name2", "photo", "name3", "id1", "id2", "id3"],
                         [["json_scope", "available", "Bob", "doggie", "string", "Williams", 358, 819, 294],
                          ["json_scope", "pending", "Billy", "doggie", "string", "Robert", 328, 549, 124],
                          ["json_scope", "sold", "Marta", "doggie", "string", "Jack", 3998, 9849, 1524]],
                         indirect=["json_scope"])
def test_pet_put1(json_scope, status, name1, name2, photo, name3, id1, id2, id3):
    fixture_execute = json_scope(json_scope, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = put(ConfigBaseUrl.base_url, json=fixture_execute)

    assert test_request.status_code == 400


@pytest.mark.parametrize(["json_scope", "status", "name1", "name2", "photo", "name3", "id1", "id2", "id3"],
                         [["json_scope", "available", "Bob", "doggie", "string", "Williams", 358, 819, 294],
                          ["json_scope", "pending", "Billy", "doggie", "string", "Robert", 328, 549, 124],
                          ["json_scope", "sold", "Marta", "doggie", "string", "Jack", 3998, 9849, 1524]],
                         indirect=["json_scope"])
def test_pet_post5(json_scope, status, name1, name2, photo, name3, id1, id2, id3):
    fixture_execute = json_scope(json_scope, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = put(ConfigBaseUrl.base_url, json=fixture_execute)

    assert test_request.headers == ConfigHeaders.headers


@pytest.mark.parametrize(["json_scope", "status", "name1", "name2", "photo", "name3", "id1", "id2", "id3"],
                         [["json_scope", "available", "Bob", "doggie", "string", "Williams", 358, 819, 294],
                          ["json_scope", "pending", "Billy", "doggie", "string", "Robert", 328, 549, 124],
                          ["json_scope", "sold", "Marta", "doggie", "string", "Jack", 3998, 9849, 1524]],
                         indirect=["json_scope"])
def test_pet_post6(json_scope, status, name1, name2, photo, name3, id1, id2, id3):
    fixture_execute = json_scope(json_scope, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = put(ConfigBaseUrl.base_url, json=fixture_execute)
    test_output = 'Invalid ID supplied'

    assert test_output in str(test_request.content)


@pytest.mark.parametrize(["json_scope", "status", "name1", "name2", "photo", "name3", "id1", "id2", "id3"],
                         [["json_scope", "available", "Harry", "doggie", "string", "Music", 0, 0, 0],
                          ["json_scope", "pending", "Pop", "doggie", "string", "Smith", 0, 0, 0],
                          ["json_scope", "sold", "Rock", "doggie", "string", "Smiley", 0, 0, 0]],
                         indirect=["json_scope"])
def test_pet_put1(json_scope, status, name1, name2, photo, name3, id1, id2, id3):
    fixture_execute = json_scope(json_scope, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = put(ConfigBaseUrl.base_url, json=fixture_execute)

    assert test_request.status_code == 404


@pytest.mark.parametrize(["json_scope", "status", "name1", "name2", "photo", "name3", "id1", "id2", "id3"],
                         [["json_scope", "available", "Bob", "doggie", "string", "Williams", 358, 819, 294],
                          ["json_scope", "pending", "Billy", "doggie", "string", "Robert", 328, 549, 124],
                          ["json_scope", "sold", "Marta", "doggie", "string", "Jack", 3998, 9849, 1524]],
                         indirect=["json_scope"])
def test_pet_post5(json_scope, status, name1, name2, photo, name3, id1, id2, id3):
    fixture_execute = json_scope(json_scope, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = put(ConfigBaseUrl.base_url, json=fixture_execute)

    assert test_request.headers == ConfigHeaders.headers


@pytest.mark.parametrize(["json_scope", "status", "name1", "name2", "photo", "name3", "id1", "id2", "id3"],
                         [["json_scope", "available", "Bob", "doggie", "string", "Williams", 358, 819, 294],
                          ["json_scope", "pending", "Billy", "doggie", "string", "Robert", 328, 549, 124],
                          ["json_scope", "sold", "Marta", "doggie", "string", "Jack", 3998, 9849, 1524]],
                         indirect=["json_scope"])
def test_pet_post6(json_scope, status, name1, name2, photo, name3, id1, id2, id3):
    fixture_execute = json_scope(json_scope, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = put(ConfigBaseUrl.base_url, json=fixture_execute)
    test_output = 'Pet not found'

    assert test_output in str(test_request.content)


@pytest.mark.parametrize(["json_scope", "status", "name1", "name2", "photo", "name3", "id1", "id2", "id3"],
                         [["json_scope", "available", 20823, "doggie", 1289230, 12089, 0, 0, 0],
                          ["json_scope", "pending", 280894, "doggie", 9218398, 982189, 0, 0, 0],
                          ["json_scope", "sold", 90289, "doggie", 2183908, 982139, 0, 0, 0]],
                         indirect=["json_scope"])
def test_pet_put1(json_scope, status, name1, name2, photo, name3, id1, id2, id3):
    fixture_execute = json_scope(json_scope, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = put(ConfigBaseUrl.base_url, json=fixture_execute)

    assert test_request.status_code == 405


@pytest.mark.parametrize(["json_scope", "status", "name1", "name2", "photo", "name3", "id1", "id2", "id3"],
                         [["json_scope", "available", 20823, "doggie", 1289230, 12089, 0, 0, 0],
                          ["json_scope", "pending", 280894, "doggie", 9218398, 982189, 0, 0, 0],
                          ["json_scope", "sold", 90289, "doggie", 2183908, 982139, 0, 0, 0]],
                         indirect=["json_scope"])
def test_pet_post5(json_scope, status, name1, name2, photo, name3, id1, id2, id3):
    fixture_execute = json_scope(json_scope, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = put(ConfigBaseUrl.base_url, json=fixture_execute)

    assert test_request.headers == ConfigHeaders.headers


@pytest.mark.parametrize(["json_scope", "status", "name1", "name2", "photo", "name3", "id1", "id2", "id3"],
                         [["json_scope", "available", 20823, "doggie", 1289230, 12089, 0, 0, 0],
                          ["json_scope", "pending", 280894, "doggie", 9218398, 982189, 0, 0, 0],
                          ["json_scope", "sold", 90289, "doggie", 2183908, 982139, 0, 0, 0]],
                         indirect=["json_scope"])
def test_pet_post6(json_scope, status, name1, name2, photo, name3, id1, id2, id3):
    fixture_execute = json_scope(json_scope, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = put(ConfigBaseUrl.base_url, json=fixture_execute)
    test_output = 'Validation exception'

    assert test_output in str(test_request.content)
