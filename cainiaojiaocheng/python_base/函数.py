"""
@FileName：函数.py
@Author：stone
@Time：2023/4/18 10:27
@Description:
"""


def hello():
    print("hello world!")


hello()


def max(a, b):
    return a if a > b else b


print(max(2, 3))


# 计算面积函数

def area(width, height):
    return width * height


print(area(4, 5))


# 传不可变对象类型


def change(a):
    print(id(a))
    a = 10
    print(id(a))


a = 1
change(a)

#  传可变类型对象  传递的是引用的地址


mylist = [1, 2, 3]
print(id(mylist))


def changeme(mylist):
    print(id(mylist))
    mylist.append([1, 2, 3])
    print(id(mylist))


changeme(mylist)

# 不定长参数

def fn1(var,*args):
    print(var)
    print(args)

fn1(1,2,3,4)



def  fn2(var,**kwargs):
    print(var)
    print(kwargs)


fn2(1,a = 2)



#  匿名函数


"""
Python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
语法
lambda 函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,.....argn]]:expression
"""

x =  lambda x:x**2

print(x(5))


sum = lambda x,y:x+y

print(sum(1,2))
