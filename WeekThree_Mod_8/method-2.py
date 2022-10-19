class Cat:
    color="White"
    about = ["Two Eyes","Wather Proof","Can be use as a hammer"]

    """ def call():
        print("Mew Mew Mew") """ ## X X Wrong
    # In the class any function making that must have a parameter self like-->
    def call(self):
        print("Mew Mew Mew")
    def feedCat(self,food):
        print(f'I am eating {food}')

my_cat = Cat()
my_cat.call()
my_cat.feedCat("Fish")