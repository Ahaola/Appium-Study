import json
import pytest
import os
import xlrd
import csv
#parametrize从json获取数据
# 获取项目路径
# BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# def read_file_from_json(file_path):
#     data = {}
#     with open(file_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#     print(f"返回的参数：{data}")
#     return data
#
# @pytest.mark.parametrize("param",read_file_from_json(BASE_PATH+"/data/case.json"))
# def test_11(param):
#     print(f"username={param['username']},password={param['password']}")


#parametrize从excel获取数据
# 获取项目路径
# BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# def read_file_from_excel(file_path, sheet_name="case01"):
#     #打开文件
#     wordbook = xlrd.open_workbook(file_path)
#     # 根据sheet名称获取sheet内容(也可以格局索引，从0开始)
#     sheet = wordbook.sheet_by_name(sheet_name)
#     # 获取第一行作为key
#     first_row = sheet.row_values(0)
#     #获取行数
#     rows_length = sheet.nrows
#     all_rows = []
#     rows_dict = []
#
#     # 获取excel行数据
#     for i in range(rows_length):
#         if i < 1:
#             continue
#         all_rows.append(sheet.row_values(i))
#     # 遍历行数据列表，生成字典
#     for row in all_rows:
#         # zip()函数用于将可迭代的对象作为参数，将对象中对应的元素（索引相同的元素）打包成一个个元组，然后返回由这些元组组成的列表
#         # 然后通过dict转换为字典
#         list1 = dict(zip(first_row, row))
#         rows_dict.append(list1)
#     return rows_dict
#
# @pytest.mark.parametrize("param",read_file_from_excel(BASE_PATH+"/data/case01.xlsx"))
# def test_11(param):
#     print(param)
#     print(f"username={param['username']},password={param['password']}")

# 获取项目路径
# BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
#
# def read_data_from_csv(file_path):
#     item = []
#     c = csv.reader(open(file_path, "r", encoding='utf-8'))
#     for i in c:
#         item.append(i)
#     print(f"返回的参数：{item}")
#     return item
#
#
# @pytest.mark.parametrize("param", read_data_from_csv(BASE_PATH + "/data/case02.csv"))
# def test_case(param):
#     print(f"name={param[0]}, work={param[1]},money={param[2]}")