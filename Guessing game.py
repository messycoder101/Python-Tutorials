# Program to guess the secret number. User gets 3 tries :)

secret_number = 9 # You can put any number here
guess_count = 0   # Initialize
guess_limit = 3   # Since user gets 3 tries
while guess_count < guess_limit:    # If number of guesses is != guess limit then,
    guess = int(input("Guess: "))   # Ask user to guess a number
    guess_count += 1                # Increment guess count
    if guess == secret_number:       # If user guesses the secret number correctly,
        print("You won!")
        break             # So that the loop stops when the user guesses the secret number correctly
else:
    print("Oh, you didn't guess the secret number!")