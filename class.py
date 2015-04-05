__author__ = 'Administrator'


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def lastname(self):
        return self.name.split()[-1]

    def age(self):
        return self.age

p = Person("chen jie", 28)
print(p.age)
print(p.lastname())