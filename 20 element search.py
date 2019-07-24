import random


def element_search():
    searchlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    keynumber = random.randint(0, 20)

    if keynumber in searchlist:
        print("Key number is in list.")

    elif keynumber not in searchlist:
        print("Key number is not in list.")


element_search()
