import pytest

# @pytest.mark.parametrize("data",[['测试'], ['测开'], ['自动化']])
# class TestTen:
#     def test_001(self, data):
#         print(f"data={data}")

#修饰器放函数上，参数值是基本类型
# @pytest.mark.parametrize("input,expected", [("1+1", 2), ("2-4", -2), ("2*3", 6)])
# def test_eval(input, expected):
#     assert eval(input) == expected

#示例二：修饰器放函数上，参数值是字典
# data = [
#     {
#         "input": "1+1",
#         "expected": 2
#     },
#     {
#         "input": "2-4",
#         "expected": -2
#     },
#     {
#         "input": "2*3",
#         "expected": 6
#     }
# ]
# @pytest.mark.parametrize("par", data)
# def test_eval(par):
#     print(f"本次入参是：input={par['input']}, expected={par['expected']}")
#     assert eval(par['input']) == par['expected']

#示例三：测试类下多个方法，会将测试数据传给此类下所有测试方法
# @pytest.mark.parametrize("name,technology", [('韧', '测试开发'), ('全栈测试笔记', '性能测试')])  # 列表嵌套元组
# class TestQzcsbj:
#     def test_case(self, name, technology):
#         print(f"test_case: name={name}, technology={technology}")
#
#     def test_case2(self, name, technology):
#         print(f"test_case2: name={name}, technology={technology}")

#调用函数获取参数数据
def get_data():
    return [('韧', '测试开发'), ('全栈测试笔记', '性能测试')]


@pytest.mark.parametrize("name,technology", get_data())
class TestQzcsbj:
    def test_case(self, name, technology):
        print(f"name={name}, technology={technology}")

#笛卡尔积：多个parametrize参数化修饰器
#应用场景：比如注册接口，考虑不同入参的组合
@pytest.mark.parametrize("username", ["qzcsbj", "ren", "jack"])
@pytest.mark.parametrize("password", ["a123", "abc123", "ABC123"])
class TestQzcsbj:
    def test_case(self, username, password):
        print(f"name={username}, technology={password}")

#笛卡尔积：parametrize与fixture混合
@pytest.fixture(params=['zhangsan', 'lisi', 'wangwu'])
def func(request):
    return request.param

@pytest.mark.parametrize("password",['123','456','789'])
class Test10:
    def test_002(self,func, password):
        print(f"name={func},password={password}")
