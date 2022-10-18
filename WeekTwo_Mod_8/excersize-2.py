class Calculator:
    def add(self,x,y):
        return x+y
    
    def substract(self,x,y):
        if y>x:  return y-x
        else:   return x-y
    
    def multiply(self,x,y):
        return x*y
    
    def divide(self,x,y):
        return x/y


test = Calculator()
print(test.add(10,20))