#!/bin/sh

# Define variables
IMAGE_NAME="vindog/da-test"
TAG="latest"  # Change this to the desired tag

# Build the Docker image
docker build -t ${IMAGE_NAME}:${TAG} .

# Log in to Docker Hub
echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin

# Push the Docker image to Docker Hub
docker push ${IMAGE_NAME}:${TAG}
