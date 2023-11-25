# Guess the number game

import random

print("Hello There..!")
name = input("What's your name?")
secretNumber = random.randint(1,77)


if name != "":
    print("well, "+name+ " are you ready to play my game (Guess my Number)?")
    Yn = input("Enter your ans (Yes/No)?")
    if (Yn == 'Y' or 'y' or 'Yes' or 'YES' or 'yes'):
        print("Game starts, I am thinking of a number from 1 to 77, And it says Guess me...")
        
        for guesses in range(1,7):
            print("Take a guess, Remember you have only 6 guesses...")
            guess = int(input("Enter your guess:"))
            
            if guess < secretNumber:
                print("Your guess is low")
            elif guess > secretNumber:
                print("Your guess is high")
            else:
                break
        
        if guess == secretNumber:
            print("Woha, "+name+" You guessed my number in limited chances...!")
        else:
            print("Nope, the number i was thinkng was:" + secretNumber + "Why don't you try another time???")
        
    else:
        print("Ohh... No, Sad to see you go..!")
else:
    print("Enter a name to proceed...")
    

