import heapq


def max_three():
    num_list = []

    for i in range(0, 3):
        element = int(input("Enter a number: "))

        num_list.append(element)
    print("The largest number in the list is ", (heapq.nlargest(1, num_list)))


max_three()
