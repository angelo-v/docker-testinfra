import docker
import pytest

testinfra_hosts = ['test_container']

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

def test_pip_packages(PipPackage):
    packages = PipPackage.get_packages()
    assert "docker" in packages
    assert "testinfra" in packages

def test_docker_executable(Command):
    assert Command.exists("docker")
