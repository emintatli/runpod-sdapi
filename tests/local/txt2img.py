#!/usr/bin/env python3
from util import post_request


if __name__ == '__main__':
    base_url = f'http://127.0.0.1:8000'

    # Create the payload dictionary
    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/sdapi/v1/txt2img"
            },
            "payload": {
                "prompt": "an astronaut riding a horse",
                "negative_prompt": "",
                "seed": -1,
                "batch_size": 1,
                "steps": 30,
                "cfg_scale": 7,
                "width": 512,
                "height": 512,
                "sampler_name": "DPM++ SDE Karras",
                "sampler_index": "DPM++ SDE Karras",
                "restore_faces": False
            }
        }
    }

    post_request(payload)
