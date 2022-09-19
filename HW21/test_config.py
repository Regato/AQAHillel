import json

import pytest

import pytz
from datetime import datetime
from datetime import timedelta

from config import ConfigBaseUrl
from config import ConfigHeaders


# /pet/{petId}


@pytest.fixture(scope="session", autouse=True)
def header_scope():
    # My time was different from the server time, so I use subtracting one second
    date_now = datetime.now(tz=pytz.timezone('UTC')) + timedelta(seconds=2)
    date_str = date_now.strftime("%a, %d %b %Y %T GMT")
    ConfigHeaders.headers = {
        'Date': f'{date_str}',
        'Content-Type': 'application/json',
        'Transfer-Encoding': 'chunked',
        'Connection': 'keep-alive',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, DELETE, PUT',
        'Access-Control-Allow-Headers': 'Content-Type, api_key, Authorization',
        'Server': 'Jetty(9.2.9.v20150224)'
    }


@pytest.fixture(scope='session', autouse=True)
def json_scope():
    def json_wrapper(*args):
        json_body = json.dumps(
            {
                "id": args[-3],
                "category":
                    {
                        "id": args[-2],
                        "name": f"{args[-7]}"
                    },
                "name": f"{args[-6]}",
                "photoUrls":
                    [
                        f"{args[-5]}"
                    ],
                "tags":
                    [
                        {
                            "id": args[-1],
                            "name": f"{args[-4]}"
                        }
                    ],
                "status": f"{args[-8]}"
            }
        )

        return json_body

    return json_wrapper
