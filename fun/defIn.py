__author__ = 'Administrator'
'''
    内部嵌套
'''
x = 2  # 定义一个全局变量


def func1():
    x = 1

    def func2():
        print(x)  # 根据LEGB发则,先找到func1中的局部
    func2()

func1()


'''
    返回函数
'''
def func3():
    x = 1

    def func4():
        print(x)
    return func4  # 返回函数

func5 = func3()  # 接收
func5()  # 调用