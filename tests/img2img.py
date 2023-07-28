#!/usr/bin/env python3
import sys

from util import *


if __name__ == '__main__':
    image_content = encode_image_to_base64('../data/src.jpg')

    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/sdapi/v1/img2img"
            },
            "payload": {
                "init_images": [
                    image_content
                ],
                "prompt": "at the ocean",
                "negative_prompt": "",
                "seed": -1,
                "batch_size": 1,
                "denoising_strength": 0.75,
                "steps": 30,
                "cfg_scale": 10,
                "width": 480,
                "height": 640,
                "sampler_name": "DPM++ SDE Karras",
                "sampler_index": "DPM++ SDE Karras",
                "restore_faces": True
            }
        }
    }

    post_request(payload)
