__author__ = 'Administrator'
'''
    重新赋值另一个模块的全局变量
'''
import global1

print(global1.X)

global1.X = 200  # 直接修改了global1中的X全局变量

print(global1.X)

global1.set_x(300)  # 通过函数修改

print(global1.X)
