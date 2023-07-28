## Building the Docker image

1. Sign up for a Docker hub account if you don't already have one.
2. Build the Docker image on your local machine and push to Docker hub:
```bash
docker build -t dockerhub-username/runpod-worker-a1111:1.0.0 .
docker login
docker push dockerhub-username/runpod-worker-a1111:1.0.0
```

If you're building on an M1 or M2 Mac, there will be an architecture
mismatch because they are `arm64`, but RunPod runs on `amd64`
architecture, so you will have to add the `--plaform` as follows:

```bash
docker buildx build --push -t dockerhub-username/runpod-worker-a1111:1.0.0 . --platform linux/amd64
```