# prompt user for number
num = int(input("Please enter a number to divide: "))

# adds number to range
listRange = list(range(1, num+1))

# list for divisor
divisorList = []

# if the number is in the list range, append divisors
for number in listRange:
    if num % number == 0:
        divisorList.append(number)

# print divisors of number
print("The divisors of", num, "are", divisorList)

