def calculateTime():
    
    # This first line is provided for you
    monkey_one = input("Is the first monkey smiling?:  ")
    monkey_two = input("Is the second monkey smiling?: ")

    if monkey_one == "y":
        if monkey_two == "y":
            print("Uh Oh! We're in trouble!")
        else:
            print("Yay! We're going to have a good day!")

    elif monkey_one == "n":
        if monkey_two == "n":
            print("Uh Oh! We're in trouble!")
        else:
            print("Yay! We're going to have a good day!")
    # end assignment


## If you want to test locally run > python monkeyCalculator.py

if __name__ == "__main__":
    calculateTime()
    
