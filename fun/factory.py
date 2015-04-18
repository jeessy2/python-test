__author__ = 'Administrator'
'''
    工厂函数
'''


def fac(N):

    def facinner(M):
        return N ** M
    return facinner

f = fac(2)  # 获得内部函数，状态信息会被保留
print(f(3))  # 2**3
# 等于下面的表达式
print(fac(2)(3))
