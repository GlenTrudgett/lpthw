""" Loops and Lists """

# Exercise 32 (study question 2) - Loops and Lists

# Could you have avoided that for-loop entirely on line 22 and just assigned
# range(0,6) directly to the elements?

# let's try!!

elements = []
print(elements)
elements = range(0, 6)
print(elements)


# This doesn't appear to  work and you need to use the for-loop to iterate through.
# trying something explicit

elements = list(range(0, 6))
print(elements)
