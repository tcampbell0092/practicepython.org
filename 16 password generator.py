# import random module for password generation
import random


# chooses either one of the two passwords in the list
def firstpass():
    passlist = random.choice(['legit', 'password'])
    print(passlist)


# makes a random password out of the given characters of a specific length
def secondpass():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = 8
    p = "".join(random.sample(s, passlen))
    print(p)


# asks user if they want a strong or weak password
def choice():
    userchoice = input("Do you want a weak or strong password? ")
    if userchoice == 'weak':
        firstpass()
    if userchoice == 'strong':
        secondpass()


choice()
