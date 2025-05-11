# Python - Slicing String
print(10*'=', "Python - Slicing String", 10*'=')

# Slicing
print("# Slicing")
print("""
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
""")

# Example
print("""
# Example
Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
""")

print("Note: The first character has index 0.")

# Slice From the Start
print(10*'=', "Slice From the Start", 10*'=')

print("By leaving out the start index, the range will start at the first character:")

# Example
print("""
# Example
Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])
""")

# Slice To the End
print(10*'=', "Slice To the End", 10*'=')

print("By leaving out the end index, the range will go to the end:")

print("""
# Example
Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])
""")

# Negative Indexing
print(10*'=', "Negative Indexing", 10*'=')

print("Use negative indexes to start the slice from the end of the string: ")

# Example
print("""
# Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])
""")