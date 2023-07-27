#!/usr/bin/env python3
from util import *


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
                "init_images": [
                    encode_image_to_base64('../../data/src.jpg')
                ],
                "prompt": "an astronaut riding a horse",
                "negative_prompt": "",
                "seed": -1,
                "batch_size": 1,
                "denoising_strength": 0.75,
                "steps": 30,
                "cfg_scale": 7,
                "width": 480,
                "height": 640,
                "sampler_name": "DPM++ SDE Karras",
                "sampler_index": "DPM++ SDE Karras",
                "restore_faces": True
            }
        }
    }

    post_request(payload)
