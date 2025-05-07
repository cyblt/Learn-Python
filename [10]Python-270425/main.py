# Python Strings
print(10*'=', "Python Strings", 10*'=')

print("#Strings")

print("""Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:""")

# Example
print("""
#Example
print("Hello")
print('Hello')
""")

# Quotes Inside Quotes
print(10*'=', "Quotes Inside Quotes", 10*'=')

print("You can use quotes inside a string, as long as they don't match the quotes surrounding the string:")

# Example
print("""
# Example
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
""")

# Assign String to a Variable
print("Assign String to a Variable")

print("Assigning a string to a variable is done with the variable name followed by an equal sign and the string:")

# Example
print("""
# Example
a = "Hello"
print(a)
""")

# Multiline String
print(10*'=', "Multiline Strings", 10*'=')

print("You can assign a multiline string to a variable by using three quotes:")

# Example
print('''
# Example
You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 
''')

print("Or three single quotes:")

# Example
print("""
# Example
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
""")

print("Note: in the result, the line breaks are inserted at the same position as in the code.\n")

# Strings are Arrays
print(10*'=', "String are Arrays", 10*'=')

print("""
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
""")

# Example
print("""
# Example
Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])
""")

# Looping Through a String
print(10*'=', "Looping Through a String", 10*'=')

print("Since strings are arrays, we can loop through the characters in a string, with a for loop.")

# Example
print("""
# Example
Loop through the letters in the word "banana":

 for x in "banana":
  print(x)
""")

print("Learn more about For Loops in our Python For Loops chapter")

# String Length
print(10*'=', "String Length", 10*'=')

print("To get the length of a string, use the len() function.")

# Example
print('''
# Example
The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))
''')

# Check String
print(10*'=', "Check String", 10*'=')

print("To check if a certain phrase or character is present in a string, we can use the keyword in.")

# Example
print('''
# Example
Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt) 
''')

print("Use it in an 'if' statement:")

# Example
print('''
# Example
Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
print("Yes, 'free' is present.") 
''')

print("Learn more about If statements in our Python If...Else chapter.")

# Check if NOT 
print(10*'=', "Check if NOT", 10*'=')

print("To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.")

# Example
print('''
# Example
Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
  print("expensive" not in txt) 

# Use it in an if statement:
# Example
print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
''')