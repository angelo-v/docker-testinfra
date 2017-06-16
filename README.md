# docker-testinfra

docker-testinfra is a docker image, that helps testing other docker images via [testinfra](https://testinfra.readthedocs.io/).

# Quickstart

    docker run --rm -t \
      -v /path/to/your-docker-project:/project \
      -v /var/run/docker.sock:/var/run/docker.sock:ro \
      aveltens/docker-testinfra

# Examples

Take a look at [this repo](https://github.com/angelo-v/docker-testinfra) to see how the image is used, to test itself.

# Development notes

* `./build.sh` to build the image
* `./test.sh` to test the image
