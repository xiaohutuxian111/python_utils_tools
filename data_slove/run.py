"""
@FileName：run.py
@Author：stone
@Time：2023/4/6 15:33
@Description:对xlsx的数据链表
"""

from openpyxl import load_workbook
import pandas as pd

file_path = './data2(1).xlsx'


#
# def sheet_name(file_path):
#     """获取xlsx的sheet名"""
#     try:
#         loadw = load_workbook(file_path)
#         sheet_names = loadw.get_sheet_names()
#     except Exception as e:
#         return e
#     else:
#         return sheet_names


def pd_sheet(file_path):
    df_left = pd.read_excel(file_path, engine='openpyxl', sheet_name=0)
    df_mid = pd.read_excel(file_path, engine='openpyxl', sheet_name=1)
    df_right = pd.read_excel(file_path, engine='openpyxl', sheet_name=2)

    df_t=pd.merge(df_left, df_mid, left_on="apply_risk_id", right_on="apply_risk_id")
    df_sum = pd.merge(df_t,df_right,left_on="apply_no", right_on="apply_no")
    df_sum.to_excel(file_path,sheet_name="汇总",index=False)

if __name__ == '__main__':
    file_path = './data2(1).xlsx'
