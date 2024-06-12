import allure
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

# def test_a():
#     print("---test_a")
#     assert 1 == 2
#
#
# def test_b():
#     print("---test_b")
#     assert 1 == 1
#
#
# class Test01:
#     def test_d(self):
#         print("---test_d")
#         assert False
#
#     def test_c(self):
#         print("---test_c")
#         assert "cs" in "qzcsbj"


data = [
    {
        "epic": "全栈测试笔记",
        "feature": "用户模块",
        "story": "用户注册",
        "title": "用户注册成功",
        "description": "desc - 用户注册成功",
        "severity": "critical",
        "request": {
            "url": "/qzcsbj/user/register",
            "method": "post",
            "headers": {'Content-Type': 'application/json'},
            "params": {"uname": "qzcsbj", "pwd": "123456"}
        }
    },
    {
        "epic": "全栈测试笔记",
        "feature": "用户模块",
        "story": "用户注册",
        "title": "用户注册失败",
        "description": "desc - 用户注册失败",
        "severity": "critical",
        "request": {
            "url": "/qzcsbj/user/register",
            "method": "post",
            "headers": {'Content-Type': 'application/json'},
            "params": {"uname": "ren", "pwd": "666666"}
        }
    },
    {
        "epic": "全栈测试笔记",
        "feature": "订单模块",
        "story": "查询订单",
        "title": "查询订单成功",
        "description": "desc - 查询订单成功",
        "severity": "normal",
        "request": {
            "url": "/qzcsbj/order/search",
            "method": "post",
            "headers": {'Content-Type': 'application/json'},
            "params": {"product": "thinkpad"}
        }
    }
]


@pytest.mark.parametrize('casedata', data)
class TestCase:
    def test_case(self, casedata):
        allure.dynamic.epic(casedata["epic"])
        allure.dynamic.feature(casedata["feature"])
        allure.dynamic.story(casedata["story"])
        allure.dynamic.title(casedata["title"])
        allure.dynamic.severity(casedata["severity"])
        allure.dynamic.description(casedata["description"])
        print(f"---测试数据是：{casedata['request']}")
        assert 1 == 1