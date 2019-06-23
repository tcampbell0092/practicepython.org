a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("List one contains", a)
print("List two contains", b)

overlap = []

for num in a:
    if num in b:
        overlap.append(num)

print("Your common numbers are", overlap)


