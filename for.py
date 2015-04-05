__author__ = 'Administrator'


d = {'a': 1, 'c': 3, 'b': 2}
# 取出集合
for x in d.keys():
    print(x, '==》', d[x])

for y in sorted(d):
    print(y, '==>', d[y])

for z in 'abc':
    print(z.upper())

# 列表解析表达式
p = [x ** 2 for x in [1, 2, 3, 4]]
print(p)

# 上面等同于
q = []
for x in [1, 2, 3, 4]:
    q.append(x ** 2)
print(q)
