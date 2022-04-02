def weatherProgram(weather, rating):
    if weather == "snowing":
        print("Snowing")
        if rating > 2:
            print("Happy")
        else:
            print("Sad")
    elif weather == "sunny" and rating > 2:
        print("sunny")
    elif weather == "sunny" or rating > 2:
        print("Sunny but sad")
    else:
        print("Stay indoors")

weather = input("What is the weather today? ")
rating = int(input("How is your day from 1 - 5? "))

weatherProgram(weather, rating)
