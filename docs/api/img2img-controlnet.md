# Image to Image with ControlNet

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/sdapi/v1/img2img"
    },
    "payload": {
      "init_images": [
        "base64 encoded image content"
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
      "restore_faces": False,
      "alwayson_scripts": {
        "controlnet": {
          "args": [
            {
              "module": "canny",
              "model": "control_v11p_sd15_canny",
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
```

## Response

### RUN

```json
{
  "id": "83bbc301-5dcd-4236-9293-a65cdd681858",
  "status": "IN_QUEUE"
}
```

### RUNSYNC

```json

```