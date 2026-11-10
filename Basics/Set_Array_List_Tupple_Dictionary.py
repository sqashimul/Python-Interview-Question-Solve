"""
Question No: What is the difference between a Set and Dictionary?
Set is an unordered collection data type that is iterable, mutable and has no duplicate elements. Python’s set class represents the mathematical notion of a set. Defined using curly braces {} or the set() function.
"""

my_set = {1, 2, 3}
print(my_set)

#Dictionary is a collection of key-value pairs used to store and retrieve data using unique keys. Dictionaries preserve insertion order. Defined using curly braces {} with key-value pairs.

my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)

"""
Question No: How is a dictionary different from a list?
A list is an ordered collection of items that are accessed using their index position, whereas a dictionary is an ordered collection of key-value pairs that are accessed using unique keys. Lists are suitable for storing sequential data, while dictionaries are ideal for storing data associated with meaningful keys.
"""
# List
numbers = [10, 20, 30]
print(numbers[1])

# Dictionary
student = {"name": "Emma", "marks": 95}
print(student["name"])

# Output
# 20
# Emma
"""
Question No: What is the difference between Python Arrays and Lists?
Arrays (when talking about the array module in Python) are specifically used to store a collection of numeric elements that are all of the same type. This makes them more efficient for storing large amounts of data and performing numerical computations where the type consistency is maintained.
"""
from array import array
arr = array('i', [1, 2, 3, 4])  # Array of integers
print(arr)

# Output
# array('i', [1, 2, 3, 4])

# Lists are more flexible than arrays in that they can hold elements of different types (integers, strings, objects, etc.). They come built-in with Python and do not require importing any additional modules. Lists support a variety of operations that can modify the list.

a = [1, 'hello', 3.14, [1, 2, 3]]
print(a)

# Output
# [1, 'hello', 3.14, [1, 2, 3]]
###########     Tuple    #######
"""
Question No: What is a tuple? How is it different from a list?
Answer:
Tuples are immutable, ordered collections.
Differences:
Tuples cannot change
Tuples are smaller, faster
Tuples are hashable → can be dictionary keys
Real-world use case:
Representing fixed coordinates:
"""
location = (37.7749, -122.4194)
print(location)
"""
Question No: Why are tuples faster than lists?
Answer:
Because they have a fixed size → Python doesn’t need dynamic resizing structures.
Real-world use case:
Storing constant config keys for performance:
"""
FIELDS = ("id", "name", "email")
print(FIELDS)

"""
Question No: Can tuples contain mutable items?
Answer:
Yes. Only the tuple itself is immutable.
"""
t = (1, [2,3])
t[1].append(4)  # allowed
print(t)

