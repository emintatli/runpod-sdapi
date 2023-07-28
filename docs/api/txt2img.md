# Text to Image

## Request

```json
{
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