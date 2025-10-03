# script.py
import random
import asyncio
from js import terminal_write  # provided by the page JS

# Helper: write to terminal from Python
def write(s):
    # ensure string
    terminal_write(str(s))

# Async input helper that awaits JS-provided line
async def input_async(prompt=""):
    # Ask JS to show the prompt and wait for a line
    # js.get_line returns a Promise which we can await
    from js import get_line
    # write the prompt to terminal (without newline) for nicer UX
    if prompt:
        terminal_write(prompt)
    val = await get_line()  # resolves to a JS string
    # convert JS string (which may be undefined/null) to Python str or None
    if val is None:
        return None
    return str(val)

# The original game logic adapted to use input_async and write()
async def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess_str = await input_async("Guess a number between 1 and 100: ")
            if guess_str is None:
                write("\nGame cancelled.\n")
                break
            # strip whitespace/newlines
            guess_str = guess_str.strip()
            # echo the entered line with a newline (JS prompt already wrote prompt; user typed; terminal UI will show the typed line)
            # Convert to int
            guess = int(guess_str)
            attempts += 1
            if guess < secret_number:
                write("\nToo low! Try again.\n")
            elif guess > secret_number:
                write("\nToo high! Try again.\n")
            else:
                write(f"\nCongratulations! You guessed the number in {attempts} attempts.\n")
                break
        except ValueError:
            write("\nInvalid input. Please enter a number.\n")

# Entry point expected by the HTML loader
async def run():
    write("Starting Number Guessing Game (press Ctrl+C or reload to cancel)\n")
    await number_guessing_game()
    write("Game ended.\n")
