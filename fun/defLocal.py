__author__ = 'Administrator'
'''
    作用域
'''
X = 99  # 全局
Y = 99  # 全局


def fun_b():
    z = 10   # 局部变量z
    Y = 100  # 此处改变不了
    print("局部变量", z)


def fun_c():
    global X  # 声明X为全局变量
    X = 100

fun_b()
fun_c()

print(X)
print(Y)