"""
@FileName：panda_utils.py
@Author：stone
@Time：2023/4/12 18:48
@Description:
"""
import os.path

import pandas as pd


class DataAnalyze():
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.sheet_names = []

    def read_file(self):
        """获取文件类型返回对应的datafame"""
        if not os.path.exists(self.file_path):
            print("{}: 文件不存在".format(self.file_path))
            return None
        dir_name, full_file_name = os.path.split(self.file_path)
        file_name, file_type = os.path.splitext(full_file_name)
        if file_type.lower() == '.csv':
            self.df = pd.read_csv(self.file_path)
        elif file_type.lower() == '.xlsx' or file_type.lower() == '.xlx':
            self.df = pd.read_excel(self.file_path, engine='openpyxl', sheet_name=None)
        else:
            print("{}:文件类型不正确".format(file_type))
            return None

    def get_df_sheet_names(self):
        """获取文件的sheet_names"""
        self.read_file()
        if not self.df:
            return None
        self.sheet_names = list(self.df)
        return self.sheet_names

    def read_df_sheet_name(self, sheet_name):
        """传入不同的sheet页名称获取不同df"""
        sheet_name = self.df[sheet_name]
        return sheet_name

    def merge_inner_df(self, df1, key, df2, key2):
        """两个df通过关联键连表(默认为内键连接)"""
        # merge的用法
        # pd.merge(DataFrame1, DataFrame2, how="inner", on=None, left_on=None, right_on=None, left_index=False,
        #          right_index=False, sort=False, suffixes=(’_x’, ‘_y’))
        # how: 默认为inner，可设为inner / outer / left / right
        # on：用于链接的列名，该列名必须存在于两个dataframe对象中。若未指明。则以两个表的交集作为链接键。
        # left_on: 左侧DataFrame中用作链接键的列。
        # right_on: 右侧DataFrame中用作链接键的列。
        # right_index: 右侧的行索引作为键连接
        # left_index: 左侧的行索引作为键连接
        # sort: 根据连接键对合并后的数据进行排列，默认为True
        # suffixes：对两个数据集中出现的重复列，新数据集中加上后缀_x, _y进行区别
        df = pd.merge(df1, df2, how="inner", left_on=key, right_on=key2, suffixes=('_x', '_y'))
        return df

    def join_df(self, df1, df2):
        #  左连接，以df1为主
        df_left = df1.join(df2, how='left', lsuffix='_df1', rsuffix='_df2')
        # 右连接
        # df_right = df1.join(df2, how='right', lsuffix='_df1', rsuffix='_df2')
        return df_left

    def conccat_df(self):
        # pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
        #           keys=None, levels=None, names=None, verify_integrity=False,
        #           copy=True)
        # objs：Series，DataFrame或Panel对象的序列或映射。
        # axis：{0, 1，...}，默认为0。0
        # 0 是上下链接，
        # 1 是左右链接。
        # join：{'inner'，'outer'}，默认为“outer”，outer为联合和inner为交集。
        pass

    def compare_df(self, df1, df2, key):
        """比较两个df中同一列中相同值"""
        pass

    def group_by_limit_df(self, df, name, number):
        """对某个指标分组，取前几条数据"""
        df = df.groupby(name).head(number)
        return df

    def write_df_to_xlsx_or_xlx(self, df, sheet_name):
        """将处理的数据追加写入excel"""
        with pd.ExcelWriter(self.file_path, mode='a', engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=sheet_name)

    def write_df_to_csv(self, df, sheet_name):
        """将处理的数据追加到csv中"""
        # 保存至file文件中，index=False表示文件中不添加索引，header=False表示不添加列名，mode='a+'表示在已有数据基础上添加新数据，并不覆盖已有数
        df.to_csv(self.file_path, index=False, mode='a+', header=True, sheet_name=sheet_name)

    def print_file(self):
        """输出sheet和列名"""
        dict_info = {}
        for sheet_name in self.get_df_sheet_names():
            dict_info[sheet_name] = self.read_df_sheet_name(sheet_name).columns
        return dict_info


if __name__ == '__main__':
    file_path = r'C:\Users\xiaol\Desktop\新韩\新韩银行_借呗风控策略V2.0_20230323_申请授信用信清退.xlsx'
    p = DataAnalyze(file_path)
    print(p.get_df_sheet_names())
    # p.read_df_sheet_name("Sheet1")
    print(p.print_file())
