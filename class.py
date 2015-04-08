__author__ = 'Administrator'


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def lastname(self):
        return self.name.split()[-1]

    def ageyear(self, year):
        return self.age+year

p = Person("chen jie", 28)
print(p.ageyear(1987))
print(p.lastname())