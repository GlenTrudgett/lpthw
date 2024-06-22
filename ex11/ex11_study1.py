""" Asking Questions """

# Exercise 11 - Asking Questions

print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weigh?", end=" ")
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

"""
input()
input(prompt)
If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised. Example:

>>>
s = input('--> ')  
--> Monty Python's Flying Circus
s  
"Monty Python's Flying Circus"
If the readline module was loaded, then input() will use it to provide elaborate line editing and history features.

Raises an auditing event builtins.input with argument prompt before reading input

Raises an auditing event builtins.input/result with the result after successfully reading input.

"""
