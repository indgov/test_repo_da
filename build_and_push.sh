#!/bin/sh

IMAGE_NAME="vindog/da-test"
TAG="latest"

docker build -t ${IMAGE_NAME}:${TAG} .
echo "${DOCKER_HUB_TOKEN}" | docker login -u "${DOCKER_HUB_USER}" --password-stdin

docker push ${IMAGE_NAME}:${TAG}
