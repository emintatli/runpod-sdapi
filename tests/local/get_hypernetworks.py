#!/usr/bin/env python3
from util import post_request


if __name__ == '__main__':
    base_url = f'http://127.0.0.1:8000'

    # Create the payload dictionary
    payload = {
        "input": {
            "api": {
                "method": "GET",
                "endpoint": "/sdapi/v1/hypernetworks"
            },
            "payload": {}
        }
    }

    post_request(payload)
