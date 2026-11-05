#Multiple arguments: Arguments are separated by spaces by default. The sep parameter controls the separator.

print("2", "4", "6", sep="-")

# End parameter: The end parameter controls what is printed after the last argument. The default is a newline (\n).
print("Line one", end="")
print("Line two")

print("Line one", end=" ")
print("Line two")

# Multiple values in one line:
name = "Alice"
score = 82
print("Name:", name, "Score:", score)

# Custom separator for compact output:
print("2", "4", "6", sep="-")

"""Python Syntax Basics
Copy Anchor Link
Indentation: Python uses indentation to define blocks. Four spaces per level is conventional. Mixing tabs and spaces can cause errors.

Colon: A colon (:) starts a block. The block must be indented. """
if True:
    print("indented block")

"""
Interview Questions
How do you pass multiple values to print()?
Pass them as separate arguments: print("a", "b", "c"). They are separated by spaces by default; use sep to change this.

What is the difference between sep and end in print()?
sep controls text between arguments. end controls what is printed after the last argument.

What is the default value of end in print()?
A newline character (\n). Use end="" to suppress the trailing newline.

What does print() do with non-string values?
It calls string conversion and prints the result. For example, print(2, True, [4, 6]) is valid."""