import pytest
import allure
'''
报告添加step
应用场景：ui自动化测试中，测试过程中的每个步骤可以通过step来描述，通过with allure.step():放在测试用例方法里面，测试步骤的代码需要被该语句包含

如果中间某个步骤失败，后面步骤不会执行

示例代码：
'''
@allure.epic("全栈测试笔记")
@allure.feature("用户模块")
@allure.story("注册")
class TestRigister:
    @allure.title("注册失败")
    @allure.severity("critical")
    @allure.description("desc - 注册失败")
    def test_reg_fail(self):
        with allure.step("步骤1：打开注册页面"):
            print("打开注册页面")
            allure.attach("文本信息",
                          name="文本",
                          attachment_type=allure.attachment_type.TEXT)
        with allure.step("步骤2：输入注册信息"):
            print("输入注册信息")
            allure.attach('<div class="wx"><img src="https://files-cdn.cnblogs.com/files/uncleyong/wx.bmp" alt="微信：ren168632201"></div>',
                          name="html",
                          attachment_type=allure.attachment_type.HTML)
        with allure.step("步骤3：提交注册，注册失败"):
            print("提交注册，注册失败")
            allure.attach.file("D:\测试开发工程师！！\优秀简历模版\优秀简历模板1.png",
                               name="这是图片",
                               attachment_type=allure.attachment_type.JPG,
                               extension="jpg")
            assert 1 == 1

    # @allure.title("注册成功")
    # @allure.severity("critical")
    # @allure.description("desc - 注册成功")
    # def test_reg_success(self):
    #     with allure.step("步骤1：打开注册页面"):
    #         print("打开注册页面")
    #     with allure.step("步骤2：输入注册信息"):
    #         print("输入注册信息")
    #     with allure.step("步骤3：提交注册，注册成功"):
    #         print("提交注册，注册成功")
    #         assert 1 == 1
    #
    # @allure.title("注册失败")
    # @allure.severity("critical")
    # @allure.description("desc - 注册失败")
    # def test_reg_fail(self):
    #     with allure.step("步骤1：打开注册页面"):
    #         print("打开注册页面")
    #     with allure.step("步骤2：输入注册信息"):
    #         print("输入注册信息")
    #     with allure.step("步骤3：提交注册，注册失败"):
    #         print("提交注册，注册失败")
    #         assert 1 == 2