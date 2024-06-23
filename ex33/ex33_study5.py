""" While Loops """

# Exercise 33 (Study Question 1)- While Loops

# Convert this while-loop to a function that you can call, and
# replace 6 in the test (i<6) with a variable.


# i = 0
numbers = []

# This function completely removed for-loops except at the end.


def print_numbers(limit, step):
    return list(range(0, limit, step))


numbers = print_numbers(16, 4)

print(numbers)


# while i < 6:
#    print(f"At the top i is {i}")
#    numbers.append(i)
#
#    i = i + 1
#    print("Numbers now: ", numbers)
#    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
