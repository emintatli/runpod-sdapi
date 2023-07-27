#!/usr/bin/env bash

echo "Worker Initiated"

echo "Symlinking files from Network Volume"
ln -s /runpod-volume /workspace

echo "Starting WebUI API"
source /workspace/venv/bin/activate
export LD_PRELOAD=libtcmalloc.so
python /workspace/stable-diffusion-webui/webui.py \
  --xformers \
  --skip-python-version-check \
  --skip-torch-cuda-test \
  --skip-install \
  --ckpt /model.safetensors \
  --lowram \
  --opt-sdp-attention \
  --disable-safe-unpickle \
  --port 3000 \
  --api \
  --nowebui \
  --skip-version-check \
  --no-hashing \
  --no-download-sd-model /workspace/logs/webui.log 2>&1 &
deactivate

echo "Starting RunPod Handler"
python -u /rp_handler.py
