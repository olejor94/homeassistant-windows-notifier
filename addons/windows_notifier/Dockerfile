FROM ghcr.io/home-assistant/aarch64-base:latest

RUN apk add --no-cache python3 py3-pip
COPY run.sh /run.sh
COPY server.py /server.py
RUN chmod +x /run.sh

CMD ["/run.sh"]
