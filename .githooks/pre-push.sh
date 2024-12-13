#!/bin/sh
#
# Run the following command in the root of your project to install this pre-push hook:
# cp git-hooks/pre-push .git/hooks/pre-push; chmod 700 .git/hooks/pre-push
# @author : Mak Sophea
# @version : 1.0
#

# get the path to this script file
DIR=$(dirname "$0")

# # Load environment variables
# source ./.env

# # Confirm Docker/Podman availability
# if ! command -v "docker" >/dev/null 2>&1 && ! command -v "podman" >/dev/null 2>&1; then
#   echo "Error: Neither Docker nor Podman found. Please install one of them."
#   exit 1
# fi

# # Get Container Runner
# RUNNER=$(command -v podman || command -v docker)  # Use whichever is available

# # Carebox
# CONTAINER_IMAGE="carebox"
# CONTAINER_NAME="carebox"
# CONTAINER_PORT="8000"
# HOST_PORT="8000"

# $RUNNER build \
#     -f "docker/Dockerfile.wolfi" \
#     -t "carebox" .

# CONTAINER_ID=$($RUNNER run \
# 	--rm \
# 	--detach \
# 	--name $CONTAINER_NAME \
# 	--publish 8050:8001 \
# 	--publish $HOST_PORT:$CONTAINER_PORT \
# 	--volume carebox_data:/home/nonroot/project/ \
# 	$CONTAINER_IMAGE)

# # Check if the container started successfully
# if [[ $? -eq 0 ]]; then
#   # Print the success message with the container ID
#   echo "Container $CONTAINER_NAME started successfully with ID: $CONTAINER_ID"
#   $RUNNER kill $CONTAINER_NAME
# else
#   echo "Error starting container $CONTAINER_NAME!"
#   exit 1
# fi