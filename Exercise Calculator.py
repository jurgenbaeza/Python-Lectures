def addNumbers(numbers):
    total = 0

    for n in numbers:
        total += n
        print(n, total)
    
    return total

print(addNumbers([8, 20, 2, 100, 2, 3]))
