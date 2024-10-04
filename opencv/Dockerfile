FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

LABEL org.label-schema.name="Southwinds Tec Ltd" \
      org.label-schema.url="https://www.southwinds.ai" \
      org.label-schema.version="3.12" \
      org.label-schema.maintainer="skipper <skipper@southwinds.io>" \
      org.label-schema.description="This image contains OpenCV and additional tools for image processing."

RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
