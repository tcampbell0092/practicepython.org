# random module used for random functions
import random

# generates random number from 1 to 5 and asks for user input
number = random.randint(1, 5)
startup = input("Welcome to the guessing game! Press enter to continue or Quit to exit: ")

# keeps track of rounds
rounds = 0

# if startup does not equal quit, start game
while startup != 'Quit':
    guess = int(input("I'm guessing a number between 1 and 5. Please enter a number: "))

    if guess < number:
        print("You guessed too low. . .")
        rounds += 1

    elif guess > number:
        print("You too high. . .")
        rounds += 1

    else:
        print("You guessed right!")
        rounds += 1

    # after game is over, ask if they want to play again and print out rounds they have played
    choice = input("Play again? Press enter to continue or No to quit: ")
    if choice == 'No':
        print("Thanks for playing! You guessed", rounds, "times.")
        break
