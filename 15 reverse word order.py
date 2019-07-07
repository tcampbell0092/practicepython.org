def reverse():
    teststring = input("please enter a string: ")
    testsplit = teststring.split()
    testreverse = testsplit[::-1]
    print(" ".join(testreverse))


reverse()

