import pytest


@pytest.fixture()
def fun():
    print("---fixture")


#影响作用域内所有用例,每个测试用例执行前都会执行fun2方法
@pytest.fixture(autouse=True)
def fun2():
    print("---fixture2")


def test_a():
    print("--------------test_a")


class Test01:
    def test_b(self, fun):
        print("--------------test_b")

    def test_c(self):
        print("--------------test_c")