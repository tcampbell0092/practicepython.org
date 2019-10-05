import time

# dictionaries of birthdays
birthdays = {
    'Albert Einstein': '3/14/1879',
    'Benjamin Franklin': '1/17/1706',
    'Ada Lovelace': '12/10/1815'}

# prints out names of whose birthdays will be displayed
print("3 important figures in history are: ")
time.sleep(1)
for x in birthdays:
    print(x)
    time.sleep(0.7)

# User input for asking whose birthday they want to know
ask = input("\nWho's birthday do you want to look up? ")

# prints out birthday of choice
if ask in birthdays:
    print("The birthday of {} is: ".format(ask))
    print(birthdays[ask])


