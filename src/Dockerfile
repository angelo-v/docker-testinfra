# hadolint ignore=DL3006
FROM alpine

LABEL org.opencontainers.image.authors="Angelo Veltens <angelo.veltens@online.de>"

# hadolint ignore=DL3018
RUN apk add --no-cache docker python3 py-pip
# hadolint ignore=DL3013
RUN pip install --no-cache-dir docker && pip install --no-cache-dir pytest-testinfra

WORKDIR /project

CMD ["pytest", "--verbose"]
