__author__ = 'Administrator'

f = open("C:\\qq.txt", 'w')
f.write("hello!")
f.close()

f = open("c:\\qq.txt", 'r')
print(f.readline())
f.close()