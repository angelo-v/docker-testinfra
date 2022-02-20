import docker
import pytest

testinfra_hosts = ['docker://test_container']

@pytest.fixture(scope="module", autouse=True)
def container(client, image):
    container = client.containers.run(
        image.id,
        name="test_container",
        detach=True,
        tty=True,
        command="sh"
    )
    yield container
    container.remove(force=True)

def test_pip_packages(host):
    packages = host.pip_package.get_packages()
    assert "docker" in packages
    assert "pytest-testinfra" in packages

def test_docker_executable(host):
    assert host.exists("docker")
