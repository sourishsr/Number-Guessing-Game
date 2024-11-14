import random

def number_guessing_game():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    
    # Generate a random number within the specified range
    target_number = random.randint(lower_bound, upper_bound)
    
    # Initialize the number of attempts
    attempts = 0
    
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. Try to guess it!")
    
    # Start the game loop
    while True:
        try:
            # Take the user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is too high, too low, or correct
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {target_number} in {attempts} attempts.")
                break  # Exit the loop if the user guesses correctly
        except ValueError:
            print("Please enter a valid integer.")
        
# Run the game
number_guessing_game()
