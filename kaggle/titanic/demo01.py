"""
@FileName：demo01.py
@Author：stone
@Time：2023/4/15 18:26
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

data_tran = pd.read_csv("./train.csv")

# 获救属性和获救结果之间的关联的统计

# 看看各乘客等级获救情况
fig = plt.figure()
fig.set(alpha=0.2)

# Survives_0 = data_tran.Pclass[data_tran.Survived == 0].value_counts()
# Survives_1 = data_tran.Pclass[data_tran.Survived == 1].value_counts()
# df = pd.DataFrame({u'获救': Survives_1, u"未获救": Survives_0})
# df.plot(kind="bar", stacked=True)
# plt.title(u"各等级的乘客获救情况")
# plt.xlabel(u"乘客等级")
# plt.ylabel(u"人数")
# plt.show()


# 获救性别和获救的情况

# Survives_m = data_tran.Survived[data_tran.Sex == 'male'].value_counts()
# Survives_f = data_tran.Survived[data_tran.Sex == 'female'].value_counts()
# df = pd.DataFrame({u"男性": Survives_m, u"女性": Survives_f})
# df.plot(kind="bar", stacked=True)
# plt.title(u"按照性别看获救情况")
# plt.xlabel(u"性别")
# plt.ylabel(u"人数")
# plt.show()

# # 查看个等级性别获救情况
# plt.title(u"根据舱等级和性别的获救情况")
# ax1 = fig.add_subplot(141)
# data_tran.Survived[data_tran.Sex == "female"][data_tran.Pclass != 3].value_counts().plot(kind="bar",
#                                                                                          label="female highclass",
#                                                                                          color='#FA2479')
# ax1.set_xticklabels([u"获救", u"未获救"], rotation=0)
# ax1.legend([u"女性/高级仓"], loc="best")
#
# ax2 = fig.add_subplot(142, sharey=ax1)
# data_tran.Survived[data_tran.Sex == "female"][data_tran.Pclass != 3].value_counts().plot(kind="bar",
#                                                                                          label="female,low class",
#                                                                                          color='pink')
# ax2.set_xticklabels([u"获救", u"未获救"], rotation=0)
# ax2.legend([u"女性/低级仓"], loc="best")
#
# ax3 = fig.add_subplot(143, sharey=ax1)
# data_tran.Survived[data_tran.Sex == "male"][data_tran.Pclass != 3].value_counts().plot(kind="bar",
#                                                                                        label="female,high class",
#                                                                                        color='lightblue')
# ax3.set_xticklabels([u"获救", u"未获救"], rotation=0)
# ax3.legend([u"男性/高级仓"], loc="best")
#
# ax4 = fig.add_subplot(144, sharey=ax1)
# data_tran.Survived[data_tran.Sex == "male"][data_tran.Pclass != 3].value_counts().plot(kind="bar",
#                                                                                        label="male low class",
#                                                                                        color='steelblue')
# ax4.set_xticklabels([u"获救", u"未获救"], rotation=0)
# ax4.legend([u"男性/低级仓"], loc="best")
#
#
# plt.show()



# fig = plt.figure()
# fig.set(alpha=0.2)  # 设定图表颜色alpha参数
#
#
# # 各窗口登船港口的获取情况
# Survived_0 = data_tran.Embarked[data_tran.Survived == 0].value_counts()
# Survived_1 = data_tran.Embarked[data_tran.Survived == 1].value_counts()
# df=pd.DataFrame({u'获救':Survived_1, u'未获救':Survived_0})
# df.plot(kind='bar', stacked=True)
# plt.title(u"各登录港口乘客的获救情况")
# plt.xlabel(u"登录港口")
# plt.ylabel(u"人数")
#
# plt.show()



#  堂兄弟/妹，孩子/父母有几人，对是否获救的影响
# g = data_tran.groupby(['SibSp','Survived'])
# df = pd.DataFrame(g.count()['PassengerId'])
# print(df)
#
# g = data_tran.groupby(['SibSp','Survived'])
# df = pd.DataFrame(g.count()['PassengerId'])
# print(df)


#ticket是船票编号，应该是unique的，和最后的结果没有太大的关系，先不纳入考虑的特征范畴把
#cabin只有204个乘客有值，我们先看看它的一个分布
# print(data_tran.Cabin.value_counts())


# fig = plt.figure()
# fig.set(alpha=0.2)  # 设定图表颜色alpha参数
#
# Survived_cabin = data_tran.Survived[pd.notnull(data_tran.Cabin)].value_counts()
# Survived_nocabin = data_tran.Survived[pd.isnull(data_tran.Cabin)].value_counts()
# df=pd.DataFrame({u'有':Survived_cabin, u'无':Survived_nocabin}).transpose()
# df.plot(kind='bar', stacked=True)
# plt.title(u"按Cabin有无看获救情况")
# plt.xlabel(u"Cabin有无")
# plt.ylabel(u"人数")
# plt.show()


# 数据预处理
from sklearn.ensemble import RandomForestRegressor


### 使用 RandomForestClassifier 填补缺失的年龄属性
def set_missing_ages(df):
    # 把已有的数值型特征取出来丢进Random Forest Regressor中
    age_df = df[['Age', 'Fare', 'Parch', 'SibSp', 'Pclass']]

    # 乘客分成已知年龄和未知年龄两部分
    known_age = age_df[age_df.Age.notnull()].values
    unknown_age = age_df[age_df.Age.isnull()].values

    # y即目标年龄
    y = known_age[:, 0]

    # X即特征属性值
    X = known_age[:, 1:]

    # fit到RandomForestRegressor之中
    rfr = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)
    rfr.fit(X, y)

    # 用得到的模型进行未知年龄结果预测
    predictedAges = rfr.predict(unknown_age[:, 1::])

    # 用得到的预测结果填补原缺失数据
    df.loc[(df.Age.isnull()), 'Age'] = predictedAges

    return df, rfr
#
#
def set_Cabin_type(df):
    df.loc[(df.Cabin.notnull()), 'Cabin'] = "Yes"
    df.loc[(df.Cabin.isnull()), 'Cabin'] = "No"
    return df

data_train = pd.read_csv("./train.csv")
data_train, rfr = set_missing_ages(data_train)
data_train = set_Cabin_type(data_train)

dummies_Cabin = pd.get_dummies(data_train['Cabin'], prefix= 'Cabin')

dummies_Embarked = pd.get_dummies(data_train['Embarked'], prefix= 'Embarked')

dummies_Sex = pd.get_dummies(data_train['Sex'], prefix= 'Sex')

dummies_Pclass = pd.get_dummies(data_train['Pclass'], prefix= 'Pclass')

df = pd.concat([data_train, dummies_Cabin, dummies_Embarked, dummies_Sex, dummies_Pclass], axis=1)
df.drop(['Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)
print(df)




import sklearn.preprocessing as preprocessing
scaler = preprocessing.StandardScaler()
age_scale_param = scaler.fit(df['Age'])
df['Age_scaled'] = scaler.fit_transform(df['Age'], age_scale_param)
fare_scale_param = scaler.fit(df['Fare'])
df['Fare_scaled'] = scaler.fit_transform(df['Fare'], fare_scale_param)
print(df)



# 逻辑回归建模

from sklearn import linear_model

# 用正则取出我们要的属性值
train_df = df.filter(regex='Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
train_np = train_df.values

# y即Survival结果
y = train_np[:, 0]

# X即特征属性值
X = train_np[:, 1:]

# fit到RandomForestRegressor之中
clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
clf.fit(X, y)


print(clf)


data_test = pd.read_csv("./test.csv")
data_test.loc[ (data_test.Fare.isnull()), 'Fare' ] = 0
# 接着我们对test_data做和train_data中一致的特征变换
# 首先用同样的RandomForestRegressor模型填上丢失的年龄
tmp_df = data_test[['Age','Fare', 'Parch', 'SibSp', 'Pclass']]
null_age = tmp_df[data_test.Age.isnull()].values
# 根据特征属性X预测年龄并补上
X = null_age[:, 1:]
predictedAges = rfr.predict(X)
data_test.loc[ (data_test.Age.isnull()), 'Age' ] = predictedAges

data_test = set_Cabin_type(data_test)
dummies_Cabin = pd.get_dummies(data_test['Cabin'], prefix= 'Cabin')
dummies_Embarked = pd.get_dummies(data_test['Embarked'], prefix= 'Embarked')
dummies_Sex = pd.get_dummies(data_test['Sex'], prefix= 'Sex')
dummies_Pclass = pd.get_dummies(data_test['Pclass'], prefix= 'Pclass')


df_test = pd.concat([data_test, dummies_Cabin, dummies_Embarked, dummies_Sex, dummies_Pclass], axis=1)
df_test.drop(['Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)
df_test['Age_scaled'] = scaler.fit_transform(df_test['Age'], age_scale_param)
df_test['Fare_scaled'] = scaler.fit_transform(df_test['Fare'], fare_scale_param)
print(df_test)


test = df_test.filter(regex='Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
predictions = clf.predict(test)
result = pd.DataFrame({'PassengerId':data_test['PassengerId'].as_matrix(), 'Survived':predictions.astype(np.int32)})
result.to_csv("./logistic_regression_predictions.csv", index=False)
