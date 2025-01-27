print(10*'=', "Python Var. pt.5 Global Variables", 10*'=', "\n")

print(10*'=', "Global Variables", 10*'=')

"""
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""

x = "awesome" # This is a Global Variables

def myfunc(): # FUNCTION
    print("Python is " + x) 

myfunc()

def myFunc():
    y = 1010 # This is a Local Variables
    print(y)

myFunc()

"""
# akan eror
print(y, x)
"""

"""
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
"""

a = "AWESOME"

def MYFUNC():
    a = "FANTASTIC"
    print("Python is " + a)

MYFUNC()

print("Python is " + a)

# The Global Keyword
print("\n" + 10*'=' + " The Global Keyword " + 10*'=')

"""
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""

# If you use the global keyword, the variable belongs to the global scope:

def Func():
    global k # k will be global variable
    k = "fantasticcc"

Func()

print("Python is " + k)


l = "AWESOME"

def myfunction():
    global l
    l = "FANTASTIC"

myfunction()

print("python is " + l)
