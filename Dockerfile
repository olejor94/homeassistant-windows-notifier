FROM alpine:3.14
RUN apk add --no-cache python3 py3-pip
COPY run.sh /run.sh
COPY notifier.py /notifier.py
CMD ["sh", "/run.sh"]
