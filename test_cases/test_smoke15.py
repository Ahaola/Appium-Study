import pytest
# def test_a():
#     try:
#         assert 1/1 == 1
#     except(ValueError, ArithmeticError):
#         print("发生数字格式异常或算数异常")
#     except:
#         print("发生其它异常")
#     print("---test_a")

# 捕获特定的异常：哪怕with下面的代码发生了ZeroDivisionError类型的异常，整个用例不会认为是异常用例，认为是正常的
def test_raises1():
    with pytest.raises(ZeroDivisionError):
        1/0


# match是正则匹配
def test_raises2():
    with pytest.raises(ValueError, match='must be 0 or None'):
        raise ValueError("value must be 0 or None")


# 没有预期的异常就报错，同时，后面的代码不会被执行
def test_raises2_2():
    with pytest.raises(ValueError, match='must be 0 or None'):
        raise ZeroDivisionError("除数为0")
    print("finish")


# 多个异常放元组中
def test_raises2_3():
    with pytest.raises((ValueError, ZeroDivisionError)):
        raise ZeroDivisionError("除数为0")


# match是正则匹配，可以使用正则表达式
def test_raises3():
    with pytest.raises(ValueError, match=r'must be \d+$'):
        raise ValueError("value must be 42")


# 获取捕获的异常的细节(异常类型， 异常信息)
def test_raises4():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("value must be 42")
    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == "value must be 42"