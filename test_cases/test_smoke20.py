import pytest

'''
allure 生成测试报告

运行测试用例并收集结果
pytest test_cases\test_smoke20.py -s -q --alluredir=./result --clean-alluredir

查看报告方式一
allure serve ./result

查看报告方式二
生成最终测试报告：allure generate ./result --clean
生成allure-report目录
打开生成的最终测试报告：allure open ./allure-report
'''

def test_a():
    print("---test_a")
    assert 1 == 2


def test_b():
    print("---test_b")
    assert 1 == 1


class Test01:
    def test_d(self):
        print("---test_d")
        assert False

    def test_c(self):
        print("---test_c")
        assert "cs" in "qzcsbj"