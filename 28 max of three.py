# heapq.nlargest() returns list of n largest values
import heapq


# define function for blank list
def max_three():
    num_list = []

    # allows for 3 numbers to be entered in the list
    for i in range(0, 3):
        element = int(input("Enter a number: "))

        #  prints out largest number in list
        num_list.append(element)
    print("The largest number in the list is ", (heapq.nlargest(1, num_list)))


max_three()
