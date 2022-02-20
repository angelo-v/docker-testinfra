test: ## run testinfra tests against the project
	./test.sh

lint: ## run hadolint against the Dockerfile
	docker run --rm -i hadolint/hadolint < src/Dockerfile

build: ## build the docker image
	./build.sh

.PHONY: test lint build
