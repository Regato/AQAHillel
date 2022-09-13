import json

import pytest
from requests import get, post, put


class ConfigBaseUrl(object):
    base_url = None


class ConfigHeaders(object):
    headers = None


class ConfigPhotoUrl(object):
    photo = None


json_body = json.dumps(
    {
        "id": 358,
        "category":
            {
                "id": 819,
                "name": "string"
            },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 294,
                "name": "string"
            }
        ],
        "status": "available"
    }
)


test_request = put("https://petstore.swagger.io/v2/pet", json=json_body)

print(test_request.headers)
