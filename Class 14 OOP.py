class Character:
    def __init__(self, name, hair, eyes): #self is only in function not for the class in player1 
        self.name = name
        self.hair = hair
        self.eyes = eyes

player1 = Character("jurgen", "long", "black")
print(player1.eyes)
player2 = Character("Bob", "short", "red")
print(player2.eyes)


Character.name = input("Character name: ")
print(Character.name)

player1 = Character.name
print(player1)
