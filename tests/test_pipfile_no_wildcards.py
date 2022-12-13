from pipfile_no_wildcards.main import main, get_packages_with_wildcards


def test_get_packages_with_wildcards():
    packages = get_packages_with_wildcards(pipfile_path="./tests/bad_Pipfile")
    assert len(packages) == 3
    assert packages == ["aenum", "pywinusb", "requests"]

    packages = get_packages_with_wildcards(pipfile_path="./tests/good_Pipfile")
    assert len(packages) == 0
