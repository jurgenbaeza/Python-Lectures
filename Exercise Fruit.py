class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


def addFruit(fruit):
    total = 0

    for item in fruit:
        total += item.price
        
     #   if item in price:
      #      total += price[item]
       # else:
        #    print("Invalid")

    return total

print(addFruit([Item("Apple",3), Item("Banana", 2), Item("Strawberry", 5), Item("Pineapple", 1)]))
    
    
