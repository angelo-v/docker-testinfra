FROM alpine

LABEL org.opencontainers.image.authors="Angelo Veltens <angelo.veltens@online.de>"

RUN apk add --no-cache docker python3 py-pip
RUN pip install --no-cache-dir docker && pip install --no-cache-dir pytest-testinfra

WORKDIR /project

CMD ["pytest", "--verbose"]
