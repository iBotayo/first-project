import random

secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")
guesses_taken = 1
while guesses_taken < 7:
    print("Take a guess.")
    guess = int(input('> '))

    if guess < secret_number:
        print("Your guess is too low.")
        guesses_taken += 1
    elif guess > secret_number:
        print("Your guess is too high.")
        guesses_taken += 1
    else:
        break  # This condition is the correct guess!

if guess == secret_number:
    print(f"Good job! You guessed my number in {guesses_taken} guesses!")
else:
    print(f"Nope. The number I was thinking of was {secret_number}.")
