import pytest


'''
参数：
--count：重复运行次数，必填
--repeat-scope：默认function，还可以是class、module、session，表示重复运行的维度，比如session，表示所有用例执行完一次，然后再执行第二次；
命令：
　　pytest --count=count --repeat-scope=function
　　或者：pytest --count count --repeat-scope function
'''

@pytest.mark.repeat(3)
def test_b():
    print("---test_b")
#
#
# def test_a():
#     print("---test_a")

# class Test1:
#     def test_b(self):
#         print("类级别---test_b")
#     def test_d(self):
#         print("类级别---test_d")
# class Test2:
#     def test_a(self):
#         print("类级别---test_a")
#     def test_c(self):
#         print("类级别---test_c")