"""
Question No:
How Does Exception Handling Work With try, except, else, and finally?
What interviewers are testing: Whether you handle errors deliberately rather than catching everything blindly.

Strong answer: try wraps the code that might raise an exception. except handles specific exceptions.
 else runs only if no exception was raised. finally runs no matter what, typically for cleanup.
"""
try:
    result = int(7)
except ValueError:
    print("Not a valid integer")
else:
    print(f"Converted successfully: {result}")
finally:
    print("This always runs")

# The most important habit is catching specific exceptions rather than using a bare except:. Catching everything silently hides bugs.
# Name the exception type you expect, and let unexpected errors surface.