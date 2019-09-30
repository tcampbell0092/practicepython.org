# user enters a string, then reverses the string
pal = input("Please enter a string: ")
pal_reversed = pal[::-1]

# if the string is spelled the same way backwards then confirm palindrome, if not then confirm it is not
if pal == pal_reversed:
    print("The string is a palindrome")

else:
    print("The string is not a palindrome")

