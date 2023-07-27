import io
import time
import json
import uuid
import base64
import requests
from PIL import Image

BASE_URL = f'http://127.0.0.1:8000'
OUTPUT_FORMAT = 'JPEG'


def encode_image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        encoded_data = base64.b64encode(image_data).decode('utf-8')
        return encoded_data


def save_result_image(resp_json):
    img = Image.open(io.BytesIO(base64.b64decode(resp_json['output']['image'])))
    file_extension = 'jpeg' if OUTPUT_FORMAT == 'JPEG' else 'png'
    output_file = f'{uuid.uuid4()}.{file_extension}'

    with open(output_file, 'wb') as f:
        print(f'Saving image: {output_file}')
        img.save(f, format=OUTPUT_FORMAT)


def post_request(payload):
    r = requests.post(
        f'{BASE_URL}/runsync',
        json=payload
    )

    print(f'Status code: {r.status_code}')

    if r.status_code == 200:
        resp_json = r.json()

        if 'output' in resp_json:
            print(json.dumps(resp_json, indent=4, default=str))
        else:
            job_status = resp_json['status']
            print(f'Job status: {job_status}')

            if job_status == 'IN_QUEUE' or job_status == 'IN_PROGRESS':
                request_id = resp_json['id']
                request_in_queue = True

                while request_in_queue:
                    r = requests.get(
                        f'{BASE_URL}/status/{request_id}',
                    )

                    print(f'Status code from RunPod status endpoint: {r.status_code}')

                    if r.status_code == 200:
                        resp_json = r.json()
                        job_status = resp_json['status']

                        if job_status == 'IN_QUEUE' or job_status == 'IN_PROGRESS':
                            print(f'RunPod request {request_id} is {job_status}, sleeping for 5 seconds...')
                            time.sleep(5)
                        elif job_status == 'FAILED':
                            request_in_queue = False
                            print(f'RunPod request {request_id} failed')
                        elif job_status == 'COMPLETED':
                            request_in_queue = False
                            print(f'RunPod request {request_id} completed')
                            print(json.dumps(resp_json, indent=4, default=str))
                        elif job_status == 'TIMED_OUT':
                            request_in_queue = False
                            print(f'ERROR: RunPod request {request_id} timed out')
                        else:
                            request_in_queue = False
                            print(f'ERROR: Invalid status response from RunPod status endpoint')
                            print(json.dumps(resp_json, indent=4, default=str))
            elif job_status == 'COMPLETED' and resp_json['output']['status'] == 'error':
                print(f'ERROR: {resp_json["output"]["message"]}')
            else:
                print(json.dumps(resp_json, indent=4, default=str))
    else:
        print(f'ERROR: {r.content}')
