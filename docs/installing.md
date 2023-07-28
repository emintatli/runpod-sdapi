# Install Automatic1111 Web UI on your Network Volume

You can either launch a new pod with a Network Volume attached
by using my [Stable Diffusion Web UI](
https://runpod.io/gsc?template=ya6013lj5a&ref=2xxro4sy) custom
[RunPod](https://runpod.io?ref=2xxro4sy) template, or alternatively,
you can install it manually following instructions below.  If you
choose to use my custom template, it is **VERY IMPORTANT** to
ensure that you first create a Network Volume and then attach
it when launching the new pod in **Secure Cloud**.  You cannot
launch a pod with a Network Volume in Community Cloud.

1. [Create a RunPod Account](https://runpod.io?ref=2xxro4sy).
2. Create a [RunPod Network Volume](https://www.runpod.io/console/user/storage).
3. Attach the Network Volume to a Secure Cloud [GPU pod](https://www.runpod.io/console/gpu-secure-cloud).
4. Select a light-weight template such as RunPod Pytorch.
5. Deploy the GPU Cloud pod.
6. Once the pod is up, open a Terminal and install the required
   dependencies if you have opted for a manual installation
   (you can skip to step 7 below if you have opted to use my
   custom template):
```bash
# Clone the repo
cd /workspace
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git

# Create and activate venv
cd stable-diffusion-webui
python -m venv --system-site-packages /workspace/venv
source /workspace/venv/bin/activate

# Install Torch and xformers
pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install --no-cache-dir xformers

# Install A1111 Web UI
wget https://raw.githubusercontent.com/ashleykleynhans/runpod-worker-a1111/main/install-automatic.py
python -m install-automatic --skip-torch-cuda-test

# Clone the ControlNet Extension
git clone https://github.com/Mikubill/sd-webui-controlnet.git extensions/sd-webui-controlnet

# Install dependencies for ControlNet
cd extensions/sd-webui-controlnet
pip install -r requirements.txt
```
7. Install the Serverless dependencies:
```bash
deactivate
cd /workspace/stable-diffusion-webui
source /workspace/venv/bin/activate
pip3 install huggingface_hub runpod>=0.10.0
```
8. Download some models, for example `Deliberate v2`:
```bash
cd /workspace/stable-diffusion-webui/models/Stable-diffusion
wget -O deliberate_v2.safetensors https://civitai.com/api/download/models/15236
```
9. Download ControlNet models, for example `canny`:
```bash
mkdir -p /workspace/stable-diffusion-webui/models/ControlNet
cd /workspace/stable-diffusion-webui/models/ControlNet
wget https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny.pth
```
10. Create logs directory:
```bash
mkdir -p /workspace/logs
```
11. Install config files:
```bash
cd /workspace/stable-diffusion-webui
rm webui-user.sh config.json ui-config.json
wget https://raw.githubusercontent.com/ashleykleynhans/runpod-worker-a1111/main/webui-user.sh
wget https://raw.githubusercontent.com/ashleykleynhans/runpod-worker-a1111/main/config.json
wget https://raw.githubusercontent.com/ashleykleynhans/runpod-worker-a1111/main/ui-config.json
```
12. Run the Web UI:
```bash
deactivate
cd /workspace/stable-diffusion-webui
./webui.sh -f
```
