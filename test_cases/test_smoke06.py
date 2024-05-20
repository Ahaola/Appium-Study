import pytest


@pytest.fixture(autouse=True, scope="function")
def fun():
    print("---fixture : function-前")
    yield
    print("---fixture : function-后")


@pytest.fixture(autouse=True, scope="class")
def fun2():
    print("---fixture : class-前")
    yield
    print("---fixture : class-后")


@pytest.fixture(autouse=True, scope="module")
def fun3():
    print("---fixture : module-前")
    yield
    print("---fixture : module-后")


@pytest.fixture(autouse=True, scope="package")
def fun4():
    print("---fixture : package-前")
    yield
    print("---fixture : package-后")


@pytest.fixture(autouse=True, scope="session")
def fun5():
    print("---fixture : session-前")
    yield
    print("---fixture : session-后")


def test_a():
    print("--------------test_a")


def test_b():
    print("--------------test_b")


class Test01Scope:
    def test_c(self):
        print("--------------test_c")

    def test_d(self):
        print("--------------test_d")