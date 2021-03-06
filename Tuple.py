__author__ = 'Administrator'

"""
    元组，元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号里，元素之间用逗号隔开。
    类似java数组
"""

a = (0, 'a', 'a', 2)
print(a)

# 元组值不能改变。 a[0] = 1

# 取出其中一个值
print(a[1])


# 元组与元组相加
tup1, tup2 = (1, 2, 3), (4, 5, 6)
print(tup1 + tup2)

# 通过index查找
print(a.index(0))
# 统计a出现的次数
print(a.count('a'))