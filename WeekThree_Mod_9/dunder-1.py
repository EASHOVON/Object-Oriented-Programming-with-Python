class Person:
    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.money = money

    '''This is called Dunder method'''
    def __add__(self,other):
        return self.age+other.age


alim = Person("Alim",25,400)
dalim = Person("Dalim",24,600)

print(alim+dalim)