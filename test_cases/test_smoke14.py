import warnings
import pytest


@pytest.mark.filterwarnings("ignore:.*自定义.*")
def test_01():
    print("_____test_01")
    assert fun() == 1

@pytest.mark.filterwarnings("ignore:.*自定义.*")
def test_02():
    print("----test02")
    warnings.warn(UserWarning("default打印每个警告"))
    assert fun() == 1

#--disable-warnings：不显示警告摘要
def fun():
    print("------fun")
    warnings.warn(UserWarning("自定义warning"))
    return 1

'''
我们可以使用@pytest.mark.filterwarnings向特定测试项添加警告筛选器，这样可以做到更细节的控制警告
'''

