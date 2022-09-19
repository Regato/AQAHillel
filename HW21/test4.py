import pytest

from requests import get, delete

from config import ConfigHeaders

from test_config import header_scope
from test_config import json_scope


@pytest.fixture(scope="function", autouse=True)
def url_scope2():
    def url_wrapper(*args):
        url = f"https://petstore.swagger.io/v2/pet/{args[7]}"

        return url

    return url_wrapper


# Cannot connect to the server so used random id's
@pytest.mark.parametrize(
    [
        "json_scope", "url_scope2",
        "status", "name1",
        "name2", "photo",
        "name3", "id1",
        "id2", "id3"
    ],
    [
        [
            "json_scope", "url_scope2",
            "available", "Hendalf",
            "doggie", "string",
            "Dog", 1, 1, 1
        ],
        [
            "json_scope", "url_scope2",
            "pending", "Bilbo",
            "doggie", "string",
            "Beggins", 2, 2, 2
        ],
        [
            "json_scope", "url_scope2",
            "sold", "Frodo",
            "doggie", "string",
            "Beggins", 3, 3, 3
        ]
    ],
    indirect=["json_scope", "url_scope2"])
def test_check_pet1(json_scope, url_scope2, status, name1, name2, photo, name3, id1, id2, id3):
    url_execute = url_scope2(json_scope, url_scope2, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = delete(url_execute)

    assert test_request.status_code == 200


# Cannot connect to the server so used random id's
@pytest.mark.parametrize(
    [
        "json_scope", "url_scope2",
        "status", "name1",
        "name2", "photo",
        "name3", "id1",
        "id2", "id3"
    ],
    [
        [
            "json_scope", "url_scope2",
            "available", "Hendalf",
            "doggie", "string",
            "Dog", 1, 1, 1
        ],
        [
            "json_scope", "url_scope2",
            "pending", "Bilbo",
            "doggie", "string",
            "Beggins", 2, 2, 2
        ],
        [
            "json_scope", "url_scope2",
            "sold", "Frodo",
            "doggie", "string",
            "Beggins", 3, 3, 3
        ]
    ],
    indirect=["json_scope", "url_scope2"])
def test_check_pet1(json_scope, url_scope2, status, name1, name2, photo, name3, id1, id2, id3):
    url_execute = url_scope2(json_scope, url_scope2, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = get(url_execute)

    assert test_request.status_code == 404


# Cannot connect to the server so used random id's
@pytest.mark.parametrize(
    [
        "json_scope", "url_scope2",
        "status", "name1",
        "name2", "photo",
        "name3", "id1",
        "id2", "id3"
    ],
    [
        [
            "json_scope", "url_scope2",
            "available", "Hendalf",
            "doggie", "string",
            "Dog", 1, 1, 1
        ],
        [
            "json_scope", "url_scope2",
            "pending", "Bilbo",
            "doggie", "string",
            "Beggins", 2, 2, 2
        ],
        [
            "json_scope", "url_scope2",
            "sold", "Frodo",
            "doggie", "string",
            "Beggins", 3, 3, 3
        ]
    ],
    indirect=["json_scope", "url_scope2"])
def test_check_pet2(json_scope, url_scope2, status, name1, name2, photo, name3, id1, id2, id3):
    url_execute = url_scope2(json_scope, url_scope2, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = get(url_execute)

    assert str(test_request.headers) == str(ConfigHeaders.headers)


# Cannot connect to the server so used random id's
@pytest.mark.parametrize(
    [
        "json_scope", "url_scope2",
        "status", "name1",
        "name2", "photo",
        "name3", "id1",
        "id2", "id3"
    ],
    [
        [
            "json_scope", "url_scope2",
            "available", "Hendalf",
            "doggie", "string",
            "Dog", 1, 1, 1
        ],
        [
            "json_scope", "url_scope2",
            "pending", "Bilbo",
            "doggie", "string",
            "Beggins", 2, 2, 2
        ],
        [
            "json_scope", "url_scope2",
            "sold", "Frodo",
            "doggie", "string",
            "Beggins", 3, 3, 3
        ]
    ],
    indirect=["json_scope", "url_scope2"])
def test_check_pet3(json_scope, url_scope2, status, name1, name2, photo, name3, id1, id2, id3):
    url_execute = url_scope2(json_scope, url_scope2, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = get(url_execute)

    assert "Pet not found" in str(test_request.json())
