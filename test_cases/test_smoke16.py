import pytest

# def test_3_in():
#     assert 'cs111' in 'qzcsbj', "断言失败描述"
#
# @pytest.mark.xfail
# def test_d():
#     print("---test_d")
#     raise Exception("异常")
#
#
# @pytest.mark.xfail(reason="异常了")
# def test_c():
#     print("---test_c")
#     raise Exception("异常")
#
# @pytest.mark.xfail(raises=RuntimeError)
# def test_b():
#     print("---test_b")
#     raise RuntimeError("运行时异常")
#
#
# @pytest.mark.xfail(raises=RuntimeError)
# def test_a():
#     print("---test_a")
#     raise Exception("异常")

def test_a():
    # 捕获特定异常；采用pytest.raises上下文管理预期异常
    # 哪怕with下面的代码发生了ZeroDivisionError类型的异常，整个用例不会认为是异常用例，认为是正常的
    with pytest.raises(ZeroDivisionError):
        1/0


def test_b():
    #  可以捕获异常，获取细节（异常类型、异常信息），后面使用
    #  下面通过ex来访问异常信息
    with pytest.raises(ZeroDivisionError) as ex:
        1/0
    print("---ex:", ex.value)
    # 断言异常value值
    assert "division" in str(ex.value)
    # 断言异常类型
    assert ex.type == ZeroDivisionError


def test_c():
    # 用正则匹配异常信息
    with pytest.raises(ZeroDivisionError, match=".*division.*") as ex:
        1/0
    pass