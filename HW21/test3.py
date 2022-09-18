import pytest

from requests import put, get

from config import ConfigBaseUrl, ConfigHeaders

from test_config import json_scope1
from test_config import json_scope2


@pytest.fixture(scope="module", autouse=True)
def url_scope1():
    ConfigBaseUrl.base_url = "https://petstore.swagger.io/v2/pet"


@pytest.fixture(scope="function", autouse=True)
def url_scope2():
    def url_wrapper(*args):
        url = f"https://petstore.swagger.io/v2/pet/{args[7]}"

        return url

    return url_wrapper


@pytest.mark.parametrize(["json_scope1", "status", "name1", "name2", "photo", "name3", "id1", "id2", "id3"],
                         [["json_scope1", "available", "Hendalf", "doggie", "string", "Dog", 1, 1, 1],
                          ["json_scope1", "pending", "Bilbo", "doggie", "string", "Beggins", 2, 2, 2],
                          ["json_scope1", "sold", "Frodo", "doggie", "string", "Beggins", 3, 3, 3]],
                         indirect=["json_scope1"])
def test_create_pet(json_scope1, status, name1, name2, photo, name3, id1, id2, id3):
    fixture_execute = json_scope1(json_scope1, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = put(ConfigBaseUrl.base_url, json=fixture_execute)

    assert test_request.status_code == 200


# Cannot connect to the server so used random id's
@pytest.mark.parametrize(
    [
        "json_scope2", "url_scope2",
        "status", "name1",
        "name2", "photo",
        "name3", "id1",
        "id2", "id3"
    ],
    [
        [
            "json_scope2", "url_scope2",
            "available", "Hendalf",
            "doggie", "string",
            "Dog", 1, 1, 1
        ],
        [
            "json_scope2", "url_scope2",
            "pending", "Bilbo",
            "doggie", "string",
            "Beggins", 2, 2, 2
        ],
        [
            "json_scope2", "url_scope2",
            "sold", "Frodo",
            "doggie", "string",
            "Beggins", 3, 3, 3
        ]
    ],
    indirect=["json_scope2", "url_scope2"])
def test_check_pet1(json_scope2, url_scope2, status, name1, name2, photo, name3, id1, id2, id3):
    url_execute = url_scope2(json_scope2, url_scope2, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = get(url_execute)

    assert test_request.status_code == 200


# Cannot connect to the server so used random id's
@pytest.mark.parametrize(
    [
        "json_scope2", "url_scope2",
        "status", "name1",
        "name2", "photo",
        "name3", "id1",
        "id2", "id3"
    ],
    [
        [
            "json_scope2", "url_scope2",
            "available", "Hendalf",
            "doggie", "string",
            "Dog", 1, 1, 1
        ],
        [
            "json_scope2", "url_scope2",
            "pending", "Bilbo",
            "doggie", "string",
            "Beggins", 2, 2, 2
        ],
        [
            "json_scope2", "url_scope2",
            "sold", "Frodo",
            "doggie", "string",
            "Beggins", 3, 3, 3
        ]
    ],
    indirect=["json_scope2", "url_scope2"])
def test_check_pet2(json_scope2, url_scope2, status, name1, name2, photo, name3, id1, id2, id3):
    json_execute = json_scope2(json_scope2, url_scope2, status, name1, name2, photo, name3, id1, id2, id3)
    url_execute = url_scope2(json_scope2, url_scope2, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = get(url_execute)

    assert test_request.headers == ConfigHeaders.headers


# Cannot connect to the server so used random id's
@pytest.mark.parametrize(
    [
        "json_scope2", "url_scope2",
        "status", "name1",
        "name2", "photo",
        "name3", "id1",
        "id2", "id3"
    ],
    [
        [
            "json_scope2", "url_scope2",
            "available", "Hendalf",
            "doggie", "string",
            "Dog", 1, 1, 1
        ],
        [
            "json_scope2", "url_scope2",
            "pending", "Bilbo",
            "doggie", "string",
            "Beggins", 2, 2, 2
        ],
        [
            "json_scope2", "url_scope2",
            "sold", "Frodo",
            "doggie", "string",
            "Beggins", 3, 3, 3
        ]
    ],
    indirect=["json_scope2", "url_scope2"])
def test_check_pet3(json_scope2, url_scope2, status, name1, name2, photo, name3, id1, id2, id3):
    json_execute = json_scope2(json_scope2, url_scope2, status, name1, name2, photo, name3, id1, id2, id3)
    url_execute = url_scope2(json_scope2, url_scope2, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = get(url_execute)

    assert test_request.json() == json_execute
