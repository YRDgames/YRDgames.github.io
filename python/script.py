import random

# Store game state
secret_number = random.randint(1, 100)
attempts = 0

def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0

def run(guess=None):
    """Called from JavaScript: pass guess as a string"""
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
                output = f"Congratulations! You guessed it in {attempts} attempts."
                reset_game()
        except ValueError:
            output = "Invalid input! Please enter a number."
    return output
