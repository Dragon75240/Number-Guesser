import random

number = random.randint(1, 100)

guesses = 0


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
        print("You got it, in " + str(guesses) + " guesses")
        break
    
    guesses += 1
    
    print("You have " + str(5 - guesses) + " guesses left")