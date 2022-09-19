import pytest

from requests import post

from config import ConfigBaseUrl

from test_config import json_scope


@pytest.fixture(scope="module", autouse=True)
def url_scope():
    ConfigBaseUrl.base_url = "https://petstore.swagger.io/v2/pet"


@pytest.mark.parametrize(["json_scope", "status", "name1", "name2", "photo", "name3", "id1", "id2", "id3"],
                         [["json_scope", "available", "Harry", "doggie", "string", "Music", 0, 0, 0],
                          ["json_scope", "pending", "Pop", "doggie", "string", "Smith", 0, 0, 0],
                          ["json_scope", "sold", "Rock", "doggie", "string", "Smiley", 0, 0, 0]],
                         indirect=["json_scope"])
def test_create_pet(json_scope, status, name1, name2, photo, name3, id1, id2, id3):
    fixture_execute = json_scope(json_scope, status, name1, name2, photo, name3, id1, id2, id3)
    test_request = post(ConfigBaseUrl.base_url, json=fixture_execute)

    assert test_request.status_code == 200
