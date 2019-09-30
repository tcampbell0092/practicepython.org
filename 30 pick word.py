import random

# creates a list for words to go in, then chooses from list of words form 'sowpods.txt'
list_words = []
with open('sowpods.txt', 'r') as file:
    for line in file:
        list_words.append(line.strip())
        print(random.choice(list_words))



