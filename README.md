Game Logic:
The program generates a random number between a specified range (e.g., 1 to 100).
The user inputs their guess.
The program compares the guess to the generated number and gives feedback if the guess is too high, too low, or correct.
The user has multiple attempts to guess the correct number.
The game continues until the correct guess is made.

How It Works:
Random Number Generation: The random.randint(lower_bound, upper_bound) function is used to generate a random number within the given range (1 to 100).
User Input: The user is prompted to input a guess, and it is converted into an integer. If the input is not a valid integer, an error message is shown.
Feedback: The program checks if the guess is too low, too high, or correct. It provides feedback after each guess.
Game Loop: The game continues until the correct number is guessed. Each time the user guesses, the number of attempts is tracked.
Winning Condition: When the user guesses the correct number, the program congratulates them and displays the number of attempts it took.
