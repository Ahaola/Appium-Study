import pytest

@pytest.fixture(param = ['测试', '测开', '自动化'])
def fun(request):  # 必须是request这个参数名
    return request.param

class TestDemo1:
    def test_cc(self, fun):
        print(f"---这是test_cc文件,取fun函数的数据={fun}")