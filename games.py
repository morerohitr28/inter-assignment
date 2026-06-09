import random

number = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("Guess the number (1-100). You have 10 attempts!")

while attempts < max_attempts:
    guess = int(input("Enter guess: "))
    attempts += 1

    if guess < number:
        print("Too low!")

    elif guess > number:
        print("Too high!")

    else:
        print("You won!")
        break

if attempts == max_attempts and guess != number:
    print(f"You lost! Number was {number}")