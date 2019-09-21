import random
# This time, computer guesses your number


# function for guessing game
def guess():
    user_number = random.randint(1, 5)
    startup = input("What number are you thinking? Press enter to continue or enter Quit to exit: ")

    # Keeps track of rounds
    rounds = 0

    # runs loop for computer to guess number
    while startup != 'Quit':
        comp_guess = random.randint(1, 5)

        if comp_guess < user_number:
            print("I guessed too low.")
            rounds += 1

        elif comp_guess > user_number:
            print("I guessed too high.")
            rounds += 1
        elif comp_guess == user_number:
            print("Ha, I got it!")
            rounds += 1
            print("It took me ", rounds, "times to guess.")

        # decides whether or not the computer will guess again
        choice = input("Will you let me guess again? Press enter to continue or No to quit: ")
        if choice == 'No':
            print("Thanks for letting me play! I got to guess", rounds, "times.")
            break


guess()
