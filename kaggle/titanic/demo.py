"""
@FileName：demo.py
@Author：stone
@Time：2023/4/15 17:27
@Description:
"""

import pandas as pd
import numpy as np

from pandas import Series, DataFrame

import matplotlib.pyplot as plt


# 以下代码从全局设置字体为SimHei（黑体），解决显示中文问题【Windows】
# 设置font.sans-serif 或 font.family 均可
plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['font.family']=['SimHei']
# 解决中文字体下坐标轴负数的负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 读取数据信息
data_tran = pd.read_csv("./train.csv")
# print(data_tran)
print(data_tran.info)
print(data_tran.columns)
# 乘客个属性分布

fig = plt.figure()
fig.set(alpha=0.2)  # 设置图标颜色alpha参数
# 在一张大图里面分几列小图
plt.subplot2grid((2, 3),(0, 0))
#  柱状图
data_tran.Survived.value_counts().plot(kind="bar")
# 标题
plt.title(u'获取情况(1为获救)')
# 人数
plt.ylabel(u'人数')

plt.subplot2grid((2, 3), (0, 1))
data_tran.Pclass.value_counts().plot(kind="bar")
plt.ylabel(u"人数")
plt.title(u"游客等级分布")


plt.subplot2grid((2,3),(0,2))
plt.scatter(data_tran.Survived,data_tran.Age)
plt.ylabel(u'年龄')
# 显示y轴的轴线
# plt.grid(b=1,which="major",axis='y')
plt.title("按照年龄获取分布(1为获救)")

plt.subplot2grid((2,3),(1,0),colspan=2)
data_tran.Age[data_tran.Pclass == 1].plot(kind='kde')
data_tran.Age[data_tran.Pclass == 2].plot(kind='kde')
data_tran.Age[data_tran.Pclass == 3].plot(kind='kde')
plt.xlabel(u"年龄")
plt.ylabel(u"密度")
plt.title("各等级乘客的年龄分布")
plt.legend((u"头等舱",u"2等仓",u"3等仓"),loc="best")


plt.subplot2grid((2,3),(1,2))
data_tran.Embarked.value_counts().plot(kind='bar')
plt.title(u'各登船口岸上船人数')
plt.ylabel(u"人数")
plt.show()