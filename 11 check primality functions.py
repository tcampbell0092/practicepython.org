def check_primality():
    x = int(input("Please enter a number: "))
    div = []
    for y in range(1, x + 1):
        if x % y == 0:
            div.append(y)
    if len(div) > 2:
        print("This number is not prime.")

    elif x == 0 or x == 1:
        print("This number is not prime")

    else:
        print("This number is prime.")


check_primality()
