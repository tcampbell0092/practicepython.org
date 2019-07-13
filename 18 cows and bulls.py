import random


def game():

    guesscount = 0
    four_digit = str(random.randint(0, 9999)).zfill(4)

    correct = False
    while not correct:
        guess = str(input("Please enter a 4-digit number between 0000 and 9999: ")).zfill(4)
        cow, bull = 0, 0

        guesscount += 1
        for x in range(0, 4):
            tempfour_digit = four_digit[x]
            tempguess = guess[x]

            if tempfour_digit == tempguess:
                cow = cow + 1
            else:
                bull = bull + 1

        if cow == 4:
            print("You guessed correctly!")
            correct = True
        else:
            print("Cows:", cow)
            print("Bulls", bull)
            print("Try again.")


if __name__ == "__main__":
    game()
