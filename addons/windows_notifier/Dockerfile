ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
ARG BUILD_VERSION

FROM ${BUILD_FROM}

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install dependencies
RUN apk add --no-cache \
    python3 \
    py3-pip \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev

# Set work directory
WORKDIR /usr/src/app

# Copy requirements.txt
COPY requirements.txt ./

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy script
COPY notifier.py ./

# Run script
CMD ["python3", "/usr/src/app/notifier.py"]
