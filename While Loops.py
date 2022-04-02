class Human:
    def __init__(self, name) :
        self.name = name

humans = [Human("Vincent"), Human("Bob"), Human("Human"), Human("Vincent")]



index = 0
while index < len(humans):
    human = humans[index]
    if human.name == "Vincent":
        humans.pop(index)
    else:
        index += 1

for human in humans:
    print(human.name)

