__author__ = 'Administrator'

X, Y = 100, 100


def func():
    global Z
    Z = X + Y

func()
print(Z)
