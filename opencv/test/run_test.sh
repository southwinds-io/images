#!/usr/bin/env sh

## creates a container from the opencv image mounting the current folder
## then executes the test script
## the output is saved back to the current folder
docker run --rm -v "$(pwd):/app" swtec/opencv:3.12 python /app/test_opencv.py
