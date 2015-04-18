__author__ = 'Administrator'
n = 0

# while n < 1000:
#     n += 1
#     if int(n % 2) == 0:
#         print("被2整除的", n)
#     elif int(n % 3) == 0:
#         print("被3整除的", n)
#     else:
#         print("不能被整除的：", n)

# 字典
a = "a"
D = {"a": 1, "b": 2, "c": 3}
print(D[a])

if 'd' not in D:
    print("d is not in D")
else:
    print(D['d'])