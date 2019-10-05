import random

# creates a list for words to go in, then chooses from list of words form 'sowpods.txt'
list_words = []
with open('sowpods.txt', 'r') as file:
    for line in file:
        list_words.append(line.strip())


# define guessing letters
def guessletter(word, usedletters):
    letter = input('Guess your letter: ').upper()
    while True:
        if letter not in caps:
            letter = input('Your entry was not a letter, try again: ').upper()
        elif letter in usedletters:
            letter = input('You already guessed that letter. try again: ').upper()
        elif letter not in word:
            usedletters.append(letter)
            letter = input('Your letter is not in the word, try again: ').upper()
        else:
            usedletters.append(letter)
            return letter


# initializes variables used in game, including the word and characters allowed to be entered
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
usedletters = []
word = (random.choice(list_words))
cur = (["_"] * len(word))
goal = "".join(list(word))

# start game and run while word is not guessed
while cur != goal:
    print(cur)
    guess = guessletter(word, usedletters)
    newcur = ""
    for i in range(0, len(goal)):
        if goal[i] == guess:
            newcur = newcur + guess
        else:
            newcur = newcur + cur[i]
    cur = newcur
    print()

# print the guessed word and end the game
print(cur)
print("The word has been solved.")
