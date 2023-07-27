#!/usr/bin/env python3
from util import *


if __name__ == '__main__':
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
                "restore_faces": True,
                "alwayson_scripts": {
                    "controlnet": {
                        "args": [
                            {
                                "module": "canny",
                                "model": "control_v11p_sd15_canny [d14c016b]",
                                "weight": 1,
                                "resize_mode": "Crop and Resize",
                                "lowvram": False,
                                "processor_res": 512,
                                "threshold_a": 75,
                                "threshold_b": 75,
                                "guidance": 1,
                                "guidance_start": 0,
                                "guidance_end": 1,
                                "control_mode": "Balanced",
                                "pixel_perfect": False
                            }
                        ]
                    }
                }
            }
        }
    }

    post_request(payload)
