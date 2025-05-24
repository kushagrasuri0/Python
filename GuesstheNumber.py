print("Name: Kushagra Suri")
print("USN: 1AY24AI058")
print("Section: M")
import random

number_to_guess = random.randint(1, 100)
attempts = 0
guess = 0

print("Welcome to the Guess the Number Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

while guess != number_to_guess:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < number_to_guess:
        print("No! Try again.")
    elif guess > number_to_guess:
        print("NO! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
