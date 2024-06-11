import pytest

'''
pip install pytest-ordering
标记于被测试函数、方法、类：@pytest.mark.run(order=x)，根据order值来决定运行顺序
x的值可以是正数、负数、0

负数的话就是从小往大执行，比如 -3、-2、-1 那么就是-3先执行，再-2，其次-1

优先级：order=0 > order=正数 > 无order > order=负数
'''

# class Test01:
#     @pytest.mark.run(order=-1)
#     def test_c(self):
#         print("---test_c")
#
#     @pytest.mark.run(order=-3)
#     def test_b(self):
#         print("---test_b")
#
#     @pytest.mark.run(order=-2)
#     def test_a(self):
#         print("---test_a")

# class TestCase01:
#     def test_d(self):
#         print("---test_d")
#
#     def test_c(self):
#         print("---test_c")
#
#     def test_b(self):
#         print("---test_b")
#
#     def test_a(self):
#         print("---test_a")

# class TestCase03:
#         def test_d(self):
#             print("---test_d")
#
#         @pytest.mark.run(order=-3)
#         def test_c(self):
#             print("---test_c")
#
#         @pytest.mark.run(order=0)
#         def test_b(self):
#             print("---test_b")
#
#         @pytest.mark.run(order=1)
#         def test_a(self):
#             print("---test_a")


'''
分组执行
函数或者方法上加装饰器：@pytest.mark.dependency(depends=["test_xxx"])
'''
# def test_d():
#     print("---test_d")
#     pass
#
#
# @pytest.mark.dependency(depends=["test_a"])
# # @pytest.mark.dependency(depends=["test_a","test_c"])  # 可以依赖多个
# def test_b():
#     print("---test_b")
#     pass
#
#
# @pytest.mark.xfail(reason="预期失败")
# def test_a():
#     print("---test_a")
#     assert 1 == 2
#
#
# def test_c():
#     print("---test_c")
#     pass


'''
应用场景
对同一用例，要执行多个断言，查看断言是否都成功
哪怕某个断言失败，后面断言依然能执行（assert实现不了）
pip install pytest-assume
assert和assume的差异
如果使用assert，某个断言失败，后面断言不会执行
如果使用pytest.assume，某个断言失败，后面断言依然会执行

使用方式
pytest.assume(表达式)
'''
def test_assume():
    pytest.assume(1 == 1)
    pytest.assume(1 == 2)
    pytest.assume(2 == 3)


