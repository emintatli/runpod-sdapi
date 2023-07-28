# Get Samplers

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/sdapi/v1/samplers"
    },
    "payload": {}
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
{
  "delayTime": 60791,
  "executionTime": 355,
  "id": "sync-a27a8d9a-b244-4aff-907d-25d220ed00b9",
  "output": [
    {
      "aliases": [
        "k_euler_a",
        "k_euler_ancestral"
      ],
      "name": "Euler a",
      "options": {
        "uses_ensd": "True"
      }
    },
    {
      "aliases": [
        "k_euler"
      ],
      "name": "Euler",
      "options": {}
    },
    {
      "aliases": [
        "k_lms"
      ],
      "name": "LMS",
      "options": {}
    },
    {
      "aliases": [
        "k_heun"
      ],
      "name": "Heun",
      "options": {
        "second_order": "True"
      }
    },
    {
      "aliases": [
        "k_dpm_2"
      ],
      "name": "DPM2",
      "options": {
        "discard_next_to_last_sigma": "True"
      }
    },
    {
      "aliases": [
        "k_dpm_2_a"
      ],
      "name": "DPM2 a",
      "options": {
        "discard_next_to_last_sigma": "True",
        "uses_ensd": "True"
      }
    },
    {
      "aliases": [
        "k_dpmpp_2s_a"
      ],
      "name": "DPM++ 2S a",
      "options": {
        "second_order": "True",
        "uses_ensd": "True"
      }
    },
    {
      "aliases": [
        "k_dpmpp_2m"
      ],
      "name": "DPM++ 2M",
      "options": {}
    },
    {
      "aliases": [
        "k_dpmpp_sde"
      ],
      "name": "DPM++ SDE",
      "options": {
        "brownian_noise": "True",
        "second_order": "True"
      }
    },
    {
      "aliases": [
        "k_dpmpp_2m_sde_ka"
      ],
      "name": "DPM++ 2M SDE",
      "options": {
        "brownian_noise": "True"
      }
    },
    {
      "aliases": [
        "k_dpm_fast"
      ],
      "name": "DPM fast",
      "options": {
        "uses_ensd": "True"
      }
    },
    {
      "aliases": [
        "k_dpm_ad"
      ],
      "name": "DPM adaptive",
      "options": {
        "uses_ensd": "True"
      }
    },
    {
      "aliases": [
        "k_lms_ka"
      ],
      "name": "LMS Karras",
      "options": {
        "scheduler": "karras"
      }
    },
    {
      "aliases": [
        "k_dpm_2_ka"
      ],
      "name": "DPM2 Karras",
      "options": {
        "discard_next_to_last_sigma": "True",
        "scheduler": "karras",
        "second_order": "True",
        "uses_ensd": "True"
      }
    },
    {
      "aliases": [
        "k_dpm_2_a_ka"
      ],
      "name": "DPM2 a Karras",
      "options": {
        "discard_next_to_last_sigma": "True",
        "scheduler": "karras",
        "second_order": "True",
        "uses_ensd": "True"
      }
    },
    {
      "aliases": [
        "k_dpmpp_2s_a_ka"
      ],
      "name": "DPM++ 2S a Karras",
      "options": {
        "scheduler": "karras",
        "second_order": "True",
        "uses_ensd": "True"
      }
    },
    {
      "aliases": [
        "k_dpmpp_2m_ka"
      ],
      "name": "DPM++ 2M Karras",
      "options": {
        "scheduler": "karras"
      }
    },
    {
      "aliases": [
        "k_dpmpp_sde_ka"
      ],
      "name": "DPM++ SDE Karras",
      "options": {
        "brownian_noise": "True",
        "scheduler": "karras",
        "second_order": "True"
      }
    },
    {
      "aliases": [
        "k_dpmpp_2m_sde_ka"
      ],
      "name": "DPM++ 2M SDE Karras",
      "options": {
        "brownian_noise": "True",
        "scheduler": "karras"
      }
    },
    {
      "aliases": [],
      "name": "DDIM",
      "options": {
        "default_eta_is_0": "True",
        "no_sdxl": "True",
        "uses_ensd": "True"
      }
    },
    {
      "aliases": [],
      "name": "PLMS",
      "options": {
        "no_sdxl": "True"
      }
    },
    {
      "aliases": [],
      "name": "UniPC",
      "options": {
        "no_sdxl": "True"
      }
    }
  ],
  "status": "COMPLETED"
}
```