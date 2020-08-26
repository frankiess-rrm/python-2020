# importing the random number function and storing into memory
import random

right_number = int(random.randint(1, 100))

# broadcasting the correct guess, this is only for debugging
print(right_number)

# ask for name and say hello
name = input('Hey, please enter your name: ')
print("Hi, " + name + ". I'm thinking of a number between 1-100. Guess what it is: ")

while True:
    try:
        guess = int(input())
    except ValueError:
        print("Sorry, please enter only whole numbers, like 1, 2 or 67.")
        # better try again... Return to the start of the loop
        continue
    if guess < 1 or guess > 100:
        print('Sorry, enter number between 1 and 100')
        continue
    else:
        print(f'Your guess is {guess}.')
        if guess < right_number:
            print('Too low! Guess again.')
            continue
        if guess > right_number:
            print('Too high! Guess again.')
            continue
        break
print(f'You got it! It was {right_number}! Congrats!')