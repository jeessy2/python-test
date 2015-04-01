__author__ = 'Administrator'

'''
    字典（dictionary）是Python中另一个非常有用的内置数据类型。
    字典是一种映射类型（mapping type），它是一个无序的键 : 值对集合。
    关键字必须使用不可变类型，也就是说list和包含可变类型的tuple不能做关键字。
    在同一个字典中，关键字还必须互不相同。

    类似java map集合

'''

a = {}
b = {'a': 1, 'b': 2, 'c': 3}

# 取一个值
print(b['a'])

# 删除一个key
del b['a']
print(b)

# 增加一个值
b['d'] = 4
print(b)

# 排序
print("排序后的值：", sorted(b.keys()))

# 返回所有的key
print("所有的key:", b.keys())
print("所有的key:", list(b.keys()))

# 测试是否有值
print('b' in b)
print('a' not in b)