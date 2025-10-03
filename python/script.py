import random

# Keep state inside the module
secret_number = random.randint(1, 100)
attempts = 0

# run() is called from JS
def run(guess=None):
    global attempts, secret_number
    output = ""
    if guess is None:
        output = "Enter a number between 1 and 100."
    else:
        try:
            guess = int(guess)
            attempts += 1
            if guess < secret_number:
                output = "Too low! Try again."
            elif guess > secret_number:
                output = "Too high! Try again."
            else:
                output = f"Congratulations! You guessed the number in {attempts} attempts."
                # Reset for a new game
                secret_number = random.randint(1, 100)
                attempts = 0
        except ValueError:
            output = "Invalid input. Please enter a number."
    return output
