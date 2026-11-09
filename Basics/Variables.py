
"""What is the difference between == and is in Python?
Both == and is are comparison operators, but they compare different things.

== checks whether two objects have the same value.
is checks whether two variables refer to the same object in memory."""

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)

# Output
# True
# False
# True



