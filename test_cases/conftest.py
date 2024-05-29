import pytest

@pytest.fixture(autouse=False, scope="function")
def login():
    print("---登录前(局部)")
    yield
    print("---登录后(局部)")