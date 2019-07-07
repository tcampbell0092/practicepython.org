import random


def firstpass():
    passlist = random.choice(['legit', 'password'])
    print(passlist)


def secondpass():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = 8
    p = "".join(random.sample(s, passlen))
    print(p)


def choice():
    userchoice = input("Do you want a weak or strong password? ")
    if userchoice == 'weak':
        firstpass()
    if userchoice == 'strong':
        secondpass()


choice()
