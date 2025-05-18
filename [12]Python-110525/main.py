# Python - Modify Strings
print(10*'=', "Python - Modify Strings", 10*'=')

print("Python has a set of built-in methods that you can use on strings.")

# Upper Case
print(10*'=', "Upper Case",10*'=')

# Example
print("""
# Example
The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
""")
# Lower Case
print(10*'=', "Lower Case", 10*'=')

# Example
print("""
# Example
The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
""")

# Remove Whitespace
print(10*'=', "Remove Whitespace",10*'=')

print("Whitespace is the space before and/or after the actual text, and very often you want to remove this space.")

# Example
print("""
# Example
The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 
""")

# Replace String
print(10*'=', "Replace String", 10*'=')

# Example
print("""
# Example
The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
""")

# Split String
print(10*'=', "Split String", 10*'=')

print("The split() method returns a list where the text between the specified separator becomes the list items.")

# Example
print("""
# Example
The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 
""")