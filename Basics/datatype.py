"""
What is the difference between a Mutable datatype and an Immutable data type?
Mutable data types are objects whose values can be changed after they are created.
Any modification is made in place without creating a new object.
Common examples include lists, dictionaries and sets.
Immutable data types are objects whose values cannot be changed after creation.
If you modify them, Python creates a new object instead. Common examples include strings, tuples, integers and floats.
"""
# Mutable example
a = [1, 2, 3]
a.append(4)
print(a)

# Immutable example
s = "Hello"
s = s + " World"
print(s)

"""
Explanation: In the first example, the list a is modified directly by adding a new element. 
In the second example, strings are immutable, so concatenating " World" creates a new string object 
and assigns it back to s.
"""