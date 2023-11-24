# Guess the number game

import random

print("Hello There..!")
name = input("What's your name?")

if name != "":
	print("Well", name , ", Are you ready to paly Guess my Number game?")


YN = input("Yes or No")

if (YN == 'Y' or 'y' or 'Yes' or 'YES' or 'yes'):
	gameplay
else:
	print("Ohh..! No. Sad to see you go.")



def gameplay(secretNumber):
	for guesses in range (1,7): 
		print("Take a Guess, Remember you will get only 6 Guess.")
		guess = int(input("Enter your Guess number:"))
		if guess < secretNumber:
			print("Your guess is low.")
		elif guess >secretNumber:
			print("Your guess is high.")
		else:
			break

if guess == secretNumber:
	print("Woha, "+name+" You guessed my number in limited chances...!")
else:
	print("Nope, the number i was thinkng was:" + secretNumber + "Why don't you try another time???")