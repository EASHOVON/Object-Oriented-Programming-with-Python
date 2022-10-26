class Demo:
    def check(self):
        return "Demo's check "
    def display(self):
        print(self.check(),end="")
class Demo_Derived(Demo):
    def check(self):
        return "Derived's check "
Demo().display()
# Demo_Derived().display()