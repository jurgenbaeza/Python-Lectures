class Mammal:
    def __init__(self, sound):
        self.sound = sound

    def makeSound(self):
        return self.sound()

    
class Dog(Mammal):
    def __init__(self, sound):
        super().__init__(sound)
    def makeSound(self):
        return ("Bark")

class Cat(Mammal):
    def __init__(self, sound):
        super().__init__(sound)
    def makeSound(self):
        return("Meow")
    
class Pig(Mammal):
    def __init__(self, sound):
        super().__init__(sound)
    def makeSound(self):
        return("Oink")

listOfSounds = [Dog("HAHAHAH"), Cat("Meow"), Pig("Oink")]
for sounds in listOfSounds:
    print(sounds.makeSound())
