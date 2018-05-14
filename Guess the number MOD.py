import random
import time

number = random.randint(1,100)

guess = 0

counter = 0

while True:
    counter += 1
    print("Guess my number between 1 and 100")
    guess = int(input())

    if guess == number:
        print("You win!")
        print("You tried " + str(counter) + " guesses.")
        break
    elif guess < number:
        print("Too low, try again.")

    elif guess > number:
        print("Too high, try again")

