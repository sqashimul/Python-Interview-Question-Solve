
""" Question: Difference between for loop and while loop in Python
For loop: Used when we know how many times to repeat, often with lists, tuples, sets or dictionaries.
    While loop: Used when we only have an end condition and don’t know exactly how many times it will repeat.
"""
for i in range(5):
    print(i)

print()

c = 0
while c < 5:
    print(c)
    c += 1

# Output
# 0
# 1
# 2
# 3
# 4
#
# 0
# 1
# 2
# 3
# 4