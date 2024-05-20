import pytest

@pytest.fixture()
def fun():
    print("---fixture")


@pytest.fixture()
def fun2():
    print("---fixture2")

def test_a(fun):
    print("--------------test_a")


class Test01:
    def test_b(self, fun2):
        print("--------------test_b")

    @pytest.mark.usefixtures('fun2', 'fun')
    def test_fun3(self):
        print("---fixture3")