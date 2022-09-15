

def pytest_addoption(parser):
    parser.addoption("--latest", action="store", default="1")
    parser.addoption("--package", action="store", default=".")
    parser.addoption("--metadata", action="store", default=".")