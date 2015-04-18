__author__ = 'Administrator'

'''
    字典（dictionary）是Python中另一个非常有用的内置数据类型。
    字典是一种映射类型（mapping type），它是一个无序的键 : 值对集合。
    关键字必须使用不可变类型，也就是说list和包含可变类型的tuple不能做关键字。
    在同一个字典中，关键字还必须互不相同。

    类似java map集合

'''

a = {}
b = {'a': 1, 'c': 3, 'b': 2}
# 创建字典的另外一种方式
c = dict(name='chenjie', age=12)
print(c['name'])
# 创建字典的另外一种方式
d = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(d)

# 迭代
print("迭代")
for x in b:
    print(b[x])

if 'd' in b:
    print(b['d'])
else:
    print("d is 0!")

try:
    print(b['d'])
except KeyError:
    print("KeyError:d is 0")

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
if 'qq' not in b:
    print("qq is not in b!!!")

# 没有，取默认值
print(b.get('qq', 0))

# 排序
K = d.keys()
Ks = list(K)
Ks.sort()
for x in Ks:
    print(d[x])

# 字典与字典的比较
DA = {"a": 1, "b": 2}
DB = {"a": 1, "b": 3}
print(sorted(DA.items()) < sorted(DB.items()))
