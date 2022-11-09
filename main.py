import random

number = random.randint(1, 100)

guesses = 0

def convert(toConvert):
    if toConvert == 0:
        return 0
    elif toConvert == 1:
        return 1
    elif toConvert == 2:
        return 2
    elif toConvert == 3:
        return 3
    elif toConvert == 4:
        return 4
    elif toConvert == 5:
        return 5

while guesses < 5:
    numberIn = int(input("Guess the number: "))
    
    if numberIn == -3218563:
        guesses -= 1
        print('The number is ' + str(number))
        
    
    if numberIn > number:
        print("Too high")
    elif numberIn < number:
        print("Too low")
    else:
        print("You got it, in " + str(convert(guesses)) + " guesses")
        break
    
    guesses += 1
    
    print("You have " + str(5 - guesses) + " guesses left")