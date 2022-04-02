listOfNumbers = []
listOfNumbers.append(5) #adds to list
print(listOfNumbers)
listOfNumbers.append(50)
print(listOfNumbers)

listOfNumbers.insert(0, 10) #(index, number)
print(listOfNumbers)
listOfNumbers.insert(2, 10)
print(listOfNumbers)

listOfNumbers.extend([1, 2, 3, 4, 5])
print(listOfNumbers)

listOfNumbers.remove(10)
print(listOfNumbers)

listOfNumbers.remove(10)
print(listOfNumbers)

listOfNumbers.pop() #removed the last digit on the list
print(listOfNumbers)

listOfNumbers.pop(1) #you can also use it as insert (index)
print(listOfNumbers)

listOfNumbers.clear() #erases everything
print(listOfNumbers)