import random
name = input("Give me your name: ")

print(f"Welome, {name}, to the amazing, one of a kind Number Guesser!")
print("Guess a number between 1-10. Right now.")

number_to_guess = random.randint(1, 10)
guess =int(input("Here: "))

if guess == number_to_guess:
    print("You got it. Great job.")
elif guess > number_to_guess:
    print(f"You thought you ate. The correct answer was: {number_to_guess}. Get better.")
else:
    print(f"That was too low. The correct answer was: {number_to_guess}. Try again.")