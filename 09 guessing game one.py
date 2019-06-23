import random

number = random.randint(1, 5)
startup = input("Welcome to the guessing game! Press enter to continue or Quit to exit: ")


rounds = 0

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

    choice = input("Play again? Press enter to continue or No to quit: ")
    if choice == 'No':
        print("Thanks for playing! You guessed", rounds, "times.")
        break
