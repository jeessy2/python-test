__author__ = 'Administrator'
n = 0

while n < 1000:
    n += 1
    if int(n % 2) == 0:
        print("被2整除的", n)
    elif int(n % 3) == 0:
        print("被3整除的", n)
    else:
        print("不能被整除的：", n)