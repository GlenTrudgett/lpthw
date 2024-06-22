""" Asking Questions """

# Exercise 11 (Study Question 3)- Asking Questions

# you can get rid of the print statement and put the text in the ()

age = input("How old are you? ")
print("How tall are you?", end=" ")
height = input()
print("How much do you weigh?", end=" ")
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.\n\n")

little_arms = input("Do you have tinny little hands (y/n)? ")
scratch_ears = input("Can you scratch your own ears (y/n)? ")

if little_arms == "y" and scratch_ears == "n":
    print("You are a T-Rex!!!! Raaaargh!!")
