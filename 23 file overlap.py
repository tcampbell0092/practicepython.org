# function for file overlap
def file_overlap():

    # opens primenumbers.txt
    with open('primenumbers.txt', 'r') as open_file:
        num1 = open_file.read()
        num1 = list(num1.splitlines())

    # opens happynumber.txt
    with open('happynumbers.txt', 'r') as open_file:
        num2 = open_file.read()
        num2 = list(num2.splitlines())

    answer = (set(num1).intersection(num2))
    print('Your overlapping prime and happy numbers are:')
    print(answer)


file_overlap()
