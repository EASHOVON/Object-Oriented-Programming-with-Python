class Triangle:
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def perimeterOfTriangle(self):
        return self.a+self.b+self.c

t1 = Triangle(3,4,5)
print(t1.perimeterOfTriangle())