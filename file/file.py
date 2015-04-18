__author__ = 'Administrator'

f = open("C:\\qq.txt", 'w')
f.write("hello!\n")
f.write("world!\n")
f.close()

# f = open("c:\\qq.txt", 'r')
# print(f.read())
# f.close()
#
# f = open("c:\\qq.txt", 'r')
# print(f.readline())
# print(f.readline())
# f.close()

# 迭代
f = open("c:\\qq.txt", 'r')
for line in f:
    print(line)