"""
@FileName：推导式.py
@Author：stone
@Time：2023/4/18 9:50
@Description:
"""

"""
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]
或者 
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]

"""

names = ['Bob', 'Tom', 'alice', 'jerry', 'wendy', 'smith']
new_names = [ele.upper() for ele in names]
new_names_01 = [ele.upper() for ele in names if len(ele) > 3]

print(new_names)
print(new_names_01)

# 字典推导式

"""
{ key_expr: value_expr for value in collection }
或
{ key_expr: value_expr for value in collection if condition }
"""
listdemo = ['Google', 'RInnob', 'Taobo']
newdict = {key: len(key) for key in listdemo}
print(newdict)
# 集合推导式
"""
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
"""
setnew = {i ** 2 for i in range(5)}
print(setnew)

# 元组推导式
"""
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
"""

a = (i ** 2 for i in range(5))
print(a)  # 返回的是生成器对象
print(tuple(a))

list1 = ["python", 'test1', 'test2']

new_list = [ele.title() if ele.startswith('p') else ele.upper() for ele in list1]
print(new_list)
