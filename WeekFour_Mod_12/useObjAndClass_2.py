class Robot:
    def introduce_self(self):
        print('My Name is {}'.format(self.name))

Alexa = Robot()

Alexa.name = "Alexa"
Alexa.age = 2
Alexa.color = "Red"

Alexa.introduce_self()