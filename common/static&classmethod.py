# -*- coding: utf-8 -*-
# @Time    : 1/17/2022 5:15 PM
# @Author  : xuanyuxi
# @Email   : xuanyuxi@360.cn
# @File    : static&classmethod.py
# @Software: PyCharm

class A:
    def fun_a(self, x):
        print(f'executing fun_a({self}, {x})')

    @classmethod
    def fun_b(cls, x):
        print(f'executing fun_a({cls}, {x})')

    @staticmethod
    def fun_c(x):
        print(f'executing fun_a({x})')

a = A()
b = A()

a.fun_a(1)
b.fun_a(1)
a.fun_b(1)
A.fun_b(1)
a.fun_c(1)
print(a.fun_a)