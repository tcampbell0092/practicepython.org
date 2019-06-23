num = int(input("Please enter a number to divide: "))

listRange = list(range(1, num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print("The divisors of", num, "are", divisorList)

