def eatMeals(): 
    print("eat breakfast")
    print("eat lunch")
    print("eat dinner")

counter = 0   #counter starts at 0 and it will increment until loop ends
for day in range(1, 8):  #day is a counter, range is o<= day < 7 so 0, 1 .. 5 , 6
    print("Current Day: ", day)
    eatMeals()
    counter += 1   #adding 1 to counter everytime until loop ends
print("Total: ", counter)
