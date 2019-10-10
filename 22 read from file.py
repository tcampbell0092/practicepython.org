# function for name counter
def name_counter():
    name_list = []

    # opens nameslist.txt and appends
    for line in open('nameslist.txt').readlines():
        name_list.append(line.rstrip())

    # counts number of times a name occurs and prints it
    name_count = list(set(name_list))
    for name in name_count:
        print(name, 'occured', name_list.count(name), 'times')


name_counter()
