__author__ = 'Administrator'
'''
    set集合, 唯一性
    类似java set集合
'''

s = {1, 2, 3, 4, 4}
print(s)

# 成员测试
print(1 in s)
print(5 in s)

# set可以进行集合运算
a = set('abc')
b = set('cde')
# a和b的差集
print(a - b)
# a和b的交集
print(a & b)
# a和b的并集
print(a | b)
# a和b中不同时存在的元素
print(a ^ b)
