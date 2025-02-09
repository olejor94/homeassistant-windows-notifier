ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest  # Eller armv7 hvis du bruker 32-bit
ARG BUILD_VERSION

FROM ${BUILD_FROM}

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Copy root filesystem
COPY rootfs /

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
RUN apk add --no-cache \
    python3 \
    py3-pip

# Install required Python packages
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose ports if needed
EXPOSE 5000

# Run s6-overlay init
ENTRYPOINT ["/init"]
