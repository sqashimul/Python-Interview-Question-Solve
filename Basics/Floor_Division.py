"""** What is the difference between / and // in Python?
/ represents precise division (result is a floating point number)
 whereas // represents floor division (result is an integer). For Example:
"""

print(5//2)
print(5/2)

# Output
# 2
# 2.5

""" ** How do you floor a number in Python?
To floor a number in Python, you can use the math.floor() function, which returns the largest integer less than or equal to the given number.

floor() method returns the floor of x i.e., the largest integer not greater than x. 
Also, The method ceil (x) returns a ceiling value of x i.e., the smallest integer greater than or equal to x.
"""



import math

n = 3.7
F_num = math.floor(n)

print(F_num)

# Output
# 3