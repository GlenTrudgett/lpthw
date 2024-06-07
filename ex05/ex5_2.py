""" More Variables and Printing """

# Exercise 5_2 - More Variables and Printing
# Adding a metric value for the variable names


name = "Zed A. Shaw"
age = 35  # not a lie
height = 74  # Inches
weight = 180  # lbs
metric_height = height * 2.54
metric_weight = weight * 0.45359237
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
metric_total = age + metric_height + metric_weight
print(f"IMPERIAL: If I add {age}, {height}, and {weight} I get {total}")
print(
    f"METRIC: If I add {age}, {metric_height}, and {metric_weight} I get {metric_total}"
)
