# -*- coding: utf-8 -*-
# @Time    : 1/17/2022 4:49 PM
# @Author  : xuanyuxi
# @Email   : xuanyuxi@360.cn
# @File    : 函数参数传递.py
# @Software: PyCharm


"""
python不允许程序员选择采用值传递还是引用传递，python参数传递采用的是传对象引用的方式这种方式相当于值传递和引用传递的一种综合

所有的变量都可以理解为内存中一个对象的引用

类型是属于对象的，而不是变量。
对象有两种：可更改对象和不可更改对象
在python中，strings，tuples，numbers是不可更改的对象，list、dict、set是可更改的对象

当一个引用(变量)传递给函数时，函数自动复制一份引用，这个函数里的引用和外边的引用没有任何关系
在例子1中：函数把引用指向了一个不可变对象，当函数返回的时候外面的引用没有任何影响，此时相当于值传递
在例子2中：函数内的引用指向的是可变对象，对它的操作就和定位了指针地址一样，在内存里进行修改，此时相当于引用传递
"""

# 例子1
a = 1


def fun_1(a):
    print('func_in', id(a))
    a = 2  # 此时a引用中保存的值，即内存地址发生变化，由原来对象1所在的地址编程对象2所在的地址
    print('re_point', id(a), id(2))


print('func_out', id(a), id(1))

fun_1(a)

print(a)

################################################

# 例子2
b = []


def fun_2(b):
    print('func_in', id(b))
    b.append(1)


print('func_out', id(b))
fun_2(b)
print(b)
