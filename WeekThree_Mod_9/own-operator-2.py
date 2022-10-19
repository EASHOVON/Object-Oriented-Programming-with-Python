class Person:
    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.money = money
    ''' This is for Class call as like function call '''
    def __call__(self):
        return f'This is {self.name} with age {self.age} and have {self.money}'
    ''' Custom operator '''
    def __lt__(self,other):
        return self.age<other.age

alim = Person("Alim",25,400)
dalim = Person("Dalim",27,600)

print(alim<dalim)