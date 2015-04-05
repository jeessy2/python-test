__author__ = 'Administrator'


d = {'a': 1, 'c': 3, 'b': 2}
# 取出集合
for x in d.keys():
    print(x, '==》', d[x])

for y in sorted(d):
    print(y, '==>', d[y])

for z in 'abc':
    print(z.upper())