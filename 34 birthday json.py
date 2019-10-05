import json


# function to create json file
def create_json(_birthdays):
    with open('birthdays.json', 'w') as f:
        json.dump(_birthdays, f)
        f.close()


# function to read json file and return info from file
def read_json():
    with open('birthdays.json', 'r') as f:
        info = json.load(f)
        f.close()
    return info


# function for printing out people whose birthdays we are searching
def print_current_birthdays():
    print('\nSome important historic figures are: ')
    for x in read_json():
        print(x)


# gets info from json file and asks for user input
def get_birthday(_info):
    while True:
        print_current_birthdays()
        search = input("Whose birthday would you like to look up? Enter the name or press 'x' to exit: ")
        if search == 'x':
            print("Thanks for participating!")
            break
        elif search in _info:
            print(search + "'s birthday is " + _info[search])


def main():
    get_birthday(read_json())


if __name__ == "__main__":
    main()
