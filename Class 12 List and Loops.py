numbers = [5, 3, 7, 8, 1, 10, 12, 20, 30, 1] 

#print(numbers[0])
#print(numbers[1])
#print(numbers[2])
#print(numbers[3])

for i in range(0, len(numbers)):
    print(numbers[i])   #len() gives us the total # of items in a list and we can add and subtract without recounting the total

for n in numbers:     #this loop is for items that are in the list
    print(n)
