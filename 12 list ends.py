a = [5, 10, 15, 20, 25]


# returns first and last number in the list
def list_ends(l):
    l[1:-1] = []
    return l


# print first and last number in the list
print(list_ends(a))



