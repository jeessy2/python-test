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

a = [(1, 2), (3, 4), (5, 6)]
for (x, y) in a:
    print(x, y)

for x, *y, z in [("a", 'b', 'c', 'd'), ('e', 'f', 'g', 'h')]:
    print(x, y, z)

# 两个for循环
item = ["aaa", (1, 2), 'bbb']
item2 = ['bbb', "aaa"]
for i1 in item:
    for i2 in item2:
        if i1 == i2:
            print("i found ", i1)
            break
    else:
        print("i cann\'t found!", i1)
