import random

# Use this as the entry point for Pyodide
def run():
    secret_number = random.randint(1, 100)
    attempts = 0
    output = []

    # We'll simulate input with a browser prompt
    while True:
        # Use JS prompt via pyodide
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

    # Join all outputs into a single string so it can be displayed in the browser
    return "\n".join(output)
