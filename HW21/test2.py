import pytest

from requests import post, get

from config import ConfigBaseUrl
from config import ConfigHeaders

from test_config import header_scope
from test_config import json_scope


@pytest.fixture(scope="function", autouse=True)
def url_scope():
    def url_wrapper(*args):
        url = f"https://petstore.swagger.io/v2/pet/{args[7]}"

        return url

    return url_wrapper


# Cannot connect to the server so used random id's
@pytest.mark.parametrize(
    [
        "json_scope", "url_scope",
        "status", "name1",
        "name2", "photo",
        "name3", "id1",
        "id2", "id3"
    ],
    [
        [
            "json_scope", "url_scope",
            "available", "Harry",
            "doggie", "string",
            "Music", 1, 1, 1
        ],
        [
            "json_scope", "url_scope",
            "pending", "Pop",
            "doggie", "string",
            "Smith", 2, 2, 2
        ],
        [
            "json_scope", "url_scope",
            "sold", "Rock",
            "doggie", "string",
            "Smiley", 3, 3, 3
        ]
    ],
    indirect=["json_scope", "url_scope"])
def test_get_pet1(json_scope, url_scope, status, name1, name2, photo, name3, id1, id2, id3):
    url_execute = url_scope(json_scope, url_scope, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = get(url_execute)

    assert test_request.status_code == 200


# Cannot connect to the server so used random id's
@pytest.mark.parametrize(
    [
        "json_scope", "url_scope",
        "status", "name1",
        "name2", "photo",
        "name3", "id1",
        "id2", "id3"
    ],
    [
        [
            "json_scope", "url_scope",
            "available", "Harry",
            "doggie", "string",
            "Music", 1, 1, 1
        ],
        [
            "json_scope", "url_scope",
            "pending", "Pop",
            "doggie", "string",
            "Smith", 2, 2, 2
        ],
        [
            "json_scope", "url_scope",
            "sold", "Rock",
            "doggie", "string",
            "Smiley", 3, 3, 3
        ]
    ],
    indirect=["json_scope", "url_scope"])
def test_get_pet2(json_scope, url_scope, status, name1, name2, photo, name3, id1, id2, id3):
    url_execute = url_scope(json_scope, url_scope, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = get(url_execute)

    assert str(test_request.headers) == str(ConfigHeaders.headers)


# Cannot connect to the server so used random id's
@pytest.mark.parametrize(
    [
        "json_scope", "url_scope",
        "status", "name1",
        "name2", "photo",
        "name3", "id1",
        "id2", "id3"
    ],
    [
        [
            "json_scope", "url_scope",
            "available", "Harry",
            "doggie", "string",
            "Music", 1, 1, 1
        ],
        [
            "json_scope", "url_scope",
            "pending", "Pop",
            "doggie", "string",
            "Smith", 2, 2, 2
        ],
        [
            "json_scope", "url_scope",
            "sold", "Rock",
            "doggie", "string",
            "Smiley", 3, 3, 3
        ]
    ],
    indirect=["json_scope", "url_scope"])
def test_get_pet3(json_scope, url_scope, status, name1, name2, photo, name3, id1, id2, id3):
    json_execute = json_scope(json_scope, url_scope, status, name1, name2, photo, name3, id1, id2, id3)
    url_execute = url_scope(json_scope, url_scope, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = get(url_execute)

    assert test_request.json() == json_execute


