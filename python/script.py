import random

def run():
    secret_number = random.randint(1, 100)
    attempts = 0
    output = []

    # Use browser prompt for input
    while True:
        guess_str = __import__("js").prompt("Guess a number between 1 and 100:")
        if guess_str is None:
            output.append("Game cancelled.")
            break
        try:
            guess = int(guess_str)
            attempts += 1
            if guess < secret_number:
                output.append("Too low! Try again.")
            elif guess > secret_number:
                output.append("Too high! Try again.")
            else:
                output.append(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            output.append("Invalid input. Please enter a number.")

    return "\n".join(output)
