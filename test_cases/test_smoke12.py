import pytest
import platform
import sys

# data = ["ren", "qzcsbj"]
# ids = [f"ע���û���{name}" for name in data]
#
#
# @pytest.mark.parametrize("name", data, ids=ids)
# class TestQzcsbj:
#     def test_case(self, name):
#         print(f"name={name}")

# @pytest.mark.skip
# def test_12():
#     print("无参数reason跳过！！！！")
#
# @pytest.mark.skip(reason="不执行这条用例")
# def test_13():
#     print("有参数reason跳过！！！")

#代码中添加跳过
# def test_14():
#     if platform.system() == "Windows":
#         pytest.skip("win下跳过！！！")
#     print("后面的代码不执行！！！")
#
# #类级跳过
# @pytest.mark.skip(reason="类级跳过")
# class Test12:
#     def test_15(self):
#         print("类方法一跳过！！")
#     def test_16(self):
#         print("类方法二跳过！！")

'''
模块级跳过
pytest.skip(msg="原因描述", allow_module_level=False)
allow_module_level为True时，跳过当前模块
'''


# if sys.platform == "win32":
#     pytest.skip('win中该模块跳过', allow_module_level=True)
# class TestCase:
#     def test_case1(self):
#         print("test_case1---skip")
#     def test_case2(self):
#         print("test_case2---skip")
#
# def test_case3():
#     print("test_case3---skip")
#
# def test_case4():
#     print("test_case4---skip")

'''
方法：skipif(condition, reason=None)
参数：
　　condition：跳过的条件，可选
　　reason：标注跳过的原因，可选
使用方法：@pytest.mark.skipif(condition, reason="xxx")
'''
# @pytest.mark.skipif(sys.platform.startswith("win"), reason="win环境中跳过")
# def test_case1():
#     print("跳过不输出！！！！！！")
#
# @pytest.mark.skipif(sys.version_info < (3, 9), reason="python3.9以下跳过")
# def test_case2():
#     pass

'''
模块级跳过
示例：下面只能是pytestmark，不能改为其它的
'''
# pytestmark = pytest.mark.skipif(sys.platform=="win32", reason="win中该模块跳过")
# def test_case1():
#     print("test_case1---skip")
# def test_case2():
#     print("test_case2---skip")

'''
importorskip
缺少模块或者版本低于参数值就跳过
参数：
　　modname：模块名
　　minversion：要求的最低版本
　　reason：跳过原因
'''
@pytest.importorskip("requests", minversion="2.31.0")
def test_12():
    print("---importorskip")