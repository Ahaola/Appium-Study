import pytest


@pytest.fixture()
def login():
    print("---登录")


@pytest.fixture()
def fun(login):
    print("---fun")