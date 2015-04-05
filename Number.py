import decimal
import fractions
__author__ = 'Administrator'

# 除法，保留小数位
print("6/4：", 6 / 4)
# 除法，不保留小数位
print("6//4：", 6 // 4)
# 取余
print("6%4：", 6 % 4)
# 乘方
print('6的3次方：', 6 ** 3)

# 多个变量，赋值
x, y = 1, 2
print('X的值为：', x)
print('Y的值为：', y)


# 精度
# 保留小数位
decimal.getcontext().prec = 4
d = decimal.Decimal(3.14156)
print(d+1)

# 分数
f = fractions.Fraction(3, 4)
print(f)
