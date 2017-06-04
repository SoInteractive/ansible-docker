from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(File):
    present = [
        "/etc/docker",
    ]
    absent = []
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists
    if absent:
        for directory in absent:
            d = File(directory)
            assert not d.exists


def test_files(File):
    present = [
        "/etc/docker/daemon.json",
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file


def test_socket(Socket):
    assert Socket("unix:///var/run/docker.sock").is_listening


def test_service(Service):
    present = [
        "docker"
    ]
    if present:
        for service in present:
            s = Service(service)
            assert s.is_running
            assert s.is_enabled


def test_packages(Package):
    present = [
        "docker-ce"
    ]
    if present:
        for package in present:
            p = Package(package)
            assert p.is_installed
