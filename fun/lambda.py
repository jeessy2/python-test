__author__ = 'Administrator'

'''
    lambda表达式
'''


def lam():
    x = 4
    action = (lambda n: n ** x)
    return action

f = lam()

print(f(2))


def lam2():
    action = (lambda x, y: x + y)
    return action

f = lam2()
print(f(1, 2))


def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda n: i ** n)
    return acts

f = makeActions()
print(f[1](2))
print(f[2](2))

def makeActions2():
    acts = []
    for i in range(5):
        acts.append(lambda n, i1=i: i1 ** n)
    return acts

f = makeActions2()
print(f[1](2))
print(f[2](2))