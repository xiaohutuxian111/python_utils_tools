"""
@FileName：read_json.py
@Author：stone
@Time：2023/4/24 14:11
@Description:
"""
import re

import pandas as pd

import json


dict_data = None
with open('预授信.json',encoding='utf-8') as f:
    dic_data  = json.load(f)
    # print(dic_data)

pattern = "\"ruleName\":"


lis = re.findall(pattern,pattern)
print(lis)









# parsed_json = json.loads(file_contents)
# print(parsed_json)


#
# df = pd.read_json("temp.json",encoding="gbk")
# # print(df.info)
# print(df.columns)
# print(df['ruleLogs'])
#
# for  row in df['ruleLogs']:
#     print(row)
