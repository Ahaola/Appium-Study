import pytest

@pytest.mark.func
def test_001():
    print("这是方法的标记func")

@pytest.mark.cla
class Test09:
    def test_002(self):
        print("这是类的标记cla")

    def test_003(self, login):
        print("局部和全局同时配置conftest时，局部生效")