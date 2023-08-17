import time
import requests
import runpod
import shutil
import os
import uuid
import glob
from urllib.parse import urlparse
from runpod.serverless.utils.rp_validator import validate
from runpod.serverless.utils import download_files_from_urls
from runpod.serverless.modules.rp_logger import RunPodLogger
from requests.adapters import HTTPAdapter, Retry
from schemas.api import API_SCHEMA
from schemas.img2img import IMG2IMG_SCHEMA
from schemas.txt2img import TXT2IMG_SCHEMA
from schemas.options import OPTIONS_SCHEMA

BASE_URL = 'http://127.0.0.1:3000'
TIMEOUT = 600

session = requests.Session()
retries = Retry(total=10, backoff_factor=0.1, status_forcelist=[502, 503, 504])
session.mount('http://', HTTPAdapter(max_retries=retries))
logger = RunPodLogger()


# ---------------------------------------------------------------------------- #
#                              Automatic Functions                             #
# ---------------------------------------------------------------------------- #

def wait_for_service(url):
    retries = 0

    while True:
        try:
            requests.get(url)
            return
        except requests.exceptions.RequestException:
            retries += 1

            # Only log every 15 retries so the logs don't get spammed
            if retries % 15 == 0:
                logger.info('Service not ready yet. Retrying...')
        except Exception as err:
            logger.error(f'Error: {err}')

        time.sleep(0.2)


def send_get_request(endpoint):
    return session.get(
        url=f'{BASE_URL}/{endpoint}',
        timeout=TIMEOUT
    )


def send_post_request(endpoint, payload):
    return session.post(
        url=f'{BASE_URL}/{endpoint}',
        json=payload,
        timeout=TIMEOUT
    )


def validate_api(event):
    if 'api' not in event['input']:
        return {
            'errors': '"api" is a required field in the "input" payload'
        }

    api = event['input']['api']

    if type(api) is not dict:
        return {
            'errors': '"api" must be a dictionary containing "method" and "endpoint"'
        }

    api['endpoint'] = api['endpoint'].lstrip('/')

    return validate(api, API_SCHEMA)

def extract_file_name(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    file_name = path.split('/')[-1] if '/' in path else path
    return file_name


def validate_payload(event):
    method = event['input']['api']['method']
    endpoint = event['input']['api']['endpoint']
    payload = event['input']['payload']
    validated_input = payload

    # if "ckpt_file" in payload:
    #     file_name=extract_file_name(payload["ckpt_file"])
    #     downloaded_files = download_files_from_urls(str(uuid.uuid1()), payload["ckpt_file"])
    #     shutil.move(downloaded_files[0], '/runpod-volume/stable-diffusion-webui/models/Stable-diffusion/' + file_name)
    #     send_post_request("/sdapi/v1/refresh-checkpoints", {})
    #     send_post_request("/sdapi/v1/options", {
    #         "sd_model_checkpoint":file_name.replace('.ckpt', '')
    #     })
    if "ckpt_file" in payload:
        files = glob.glob('/runpod-volume/stable-diffusion-webui/models/Stable-diffusion/*')
        for f in files:
            os.remove(f)
        file_name=extract_file_name(payload["ckpt_file"])
        downloaded_files = download_files_from_urls(str(uuid.uuid1()), payload["ckpt_file"])
        shutil.move(downloaded_files[0], '/runpod-volume/stable-diffusion-webui/models/Stable-diffusion/' + file_name)
        send_post_request("sdapi/v1/refresh-checkpoints", {})
        send_get_request('sdapi/v1/sd-models')
        send_post_request("sdapi/v1/options", {
            "sd_model_checkpoint":file_name.replace('.ckpt', '')
        })
        


    if endpoint == 'txt2img':
        validated_input = validate(payload, TXT2IMG_SCHEMA)
    elif endpoint == 'img2img':
        validated_input = validate(payload, IMG2IMG_SCHEMA)
    elif endpoint == 'options' and method == 'POST':
        validated_input = validate(payload, OPTIONS_SCHEMA)

    return endpoint, event['input']['api']['method'], validated_input


# ---------------------------------------------------------------------------- #
#                                RunPod Handler                                #
# ---------------------------------------------------------------------------- #
def handler(event):

    validated_api = validate_api(event)

    if 'errors' in validated_api:
        return {
            'error': validated_api['errors']
        }

    endpoint, method, validated_input = validate_payload(event)

    if 'errors' in validated_input:
        return {
            'error': validated_input['errors']
        }

    if 'validated_input' in validated_input:
        payload = validated_input['validated_input']
    else:
        payload = validated_input

    try:
        logger.log(f'Sending {method} request to: /{endpoint}')

        if method == 'GET':
            response = send_get_request(endpoint)
        elif method == 'POST':
            response = send_post_request(endpoint, payload)
    except Exception as e:
        return {
            'error': str(e)
        }

    return response.json()


if __name__ == "__main__":
    wait_for_service(url='http://127.0.0.1:3000/sdapi/v1/sd-models')
    logger.log('Automatic1111 API is ready', 'INFO')
    logger.log('Starting RunPod Serverless...', 'INFO')
    runpod.serverless.start(
        {
            'handler': handler
        }
    )
