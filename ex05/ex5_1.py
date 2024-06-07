""" More Variables and Printing """

# Exercise 5_1 - More Variables and Printing
# Removing "my_" from the variable names


name = "Zed A. Shaw"
age = 35  # not a lie
height = 74  # Inches
weight = 180  # lbs
eyes = "Blue"
teeth = "White"
hair = "Brown"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not to heavy.")
print(f"He's got my {eyes} and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")
