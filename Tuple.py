__author__ = 'Administrator'

"""
    元组，元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号里，元素之间用逗号隔开。
"""

a = (0, 'a', 2)
print(a)

# 元组值不能改变。 a[0] = 1

# 取出其中一个值
print(a[1])


# 元组与元组相加
tup1, tup2 = (1, 2, 3), (4, 5, 6)
print(tup1 + tup2)


