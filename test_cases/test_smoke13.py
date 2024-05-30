import pytest
import sys
'''
方法：xfail(condition=None, reason=None, raises=None, run=True, strict=False)
常用参数：
condition：预期失败的条件
reason：失败的原因
run：布尔值，是否运行
raises：抛出某类型异常，和用例中raise的异常类型一样，结果就是FAILED，否则结果是XFAIL
strict，默认是False，strict=False，断言成功结果是XPASS，断言失败结果是XFAIL；strict=True，断言成功结果是FAILED，断言失败结果是XFAIL 
使用方法：
　　@pytest.mark.xfail(condition, reason="xxx" )
'''
# @pytest.mark.xfail
# def test_case1():
#     print("代码开发中")
#     assert 1==1
#
# @pytest.mark.xfail
# def test_case2():
#     print("代码开发中")
#     assert 1==2

#函数/方法执行过程中预期失败
# def test_case3():
#     print("前置条件")
#     pytest.xfail("预期函数执行失败，后续代码不再执行!!")
#     print("hahdhahdahd")
#     assert 1==2

'''
xfail方法run参数
默认是True
run=False不会执行方法
'''
# @pytest.mark.xfail(run=False)
# def test_case4():
#     print("test_case4不执行")
#
# @pytest.mark.xfail(run=True)
# def test_case5():
#     print("test_case5执行")

'''
xfail方法raises参数
raises：抛出某类型异常，如果和用例中raise的异常类型一样，结果就是XFAIL，否则结果是FAILED
'''
# @pytest.mark.xfail(raises=RuntimeError)
# def test_b():
#     print("和用例中raise的异常类型一样，结果就是FAILED")
#     raise RuntimeError("运行时异常")
#
# @pytest.mark.xfail(raises=RuntimeError)
# def test_a():
#     print("和用例中raise的异常类型不一样，结果就是XFAIL")
#     raise Exception("异常")

'''
我们可以将常用标记赋值给一个标记变量，这样可以在模块中、模块间共享这些标记变量
如果是模块间共享，需要把标记变量单独放一个文件中，然后模块中导入
'''
if_win_skip_mark = pytest.mark.skipif(sys.platform == "win32", reason="win环境中跳过")
if_below_py39_skip_mark = pytest.mark.skipif(sys.version_info < (3, 9), reason="python3.9以下跳过")
not_complete_xfail_mark = pytest.mark.xfail(reason="代码开发中")
discard_xfail_mark = pytest.mark.xfail  # 也可以不带reason

@if_win_skip_mark
def test_case1():
    print("---skipif")
    assert 1 == 1

@if_below_py39_skip_mark
def test_case2():
    print("---skipif")
    assert 1 == 1

@not_complete_xfail_mark
def test_case3():
    print("---xfail")
    assert 1 == 1

@discard_xfail_mark(reason="废弃")
def test_case4():
    print("---xfail")
    assert 1 == 1