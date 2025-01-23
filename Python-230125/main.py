print(10*'=', "Python Var. pt.4 Output Variables", 10*'=')

print(5*'=', "Output Variables", 5*'=')

# The Python print() function is often used to output variables.

a = "python is awesome"
print(a)

# In the print() function, you output multiple variables, separated by a comma:

a = "python"
b = "is"
c = "awesome"
print(a, b, c)

# You can also use the + operator to output multiple variables:

a = "python "
b = "is "
c = "awesome"
print(a + b + c)

# Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

# For numbers, the + character works as a mathematical operator:

a = 5
b = 3
print(a + b)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

"""
a = 3
b = "wkwkwk"
print(a + b)
"""

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

a = 2
b = "Dudung"
print(a, b)
