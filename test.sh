#!/bin/sh

docker run --rm -it \
  -v $(pwd):/project \
  -v /var/run/docker.sock:/var/run/docker.sock \
  aveltens/docker-testinfra sh
