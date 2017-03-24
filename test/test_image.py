import docker
import pytest

testinfra_hosts = ['test_container']

@pytest.fixture(scope="module", autouse=True)
def container(client, image):
    container = client.containers.run(
        image.id,
        name="test_container",
        detach=True
    )
    yield container
    container.remove(force=True)

def test_pip_packages(Package):
    assert Package("foo").is_installed()
