import pytest

@pytest.fixture(autouse=False, scope="function")
def login():
    print("---登录前(全局)")
    yield
    print("---登录后(全局)")