# Image to Image

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
      "restore_faces": true
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