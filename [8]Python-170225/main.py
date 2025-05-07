# Python Numbers
print(10*'=', "Python Numbers", 10*'=')

print("There are three numeric types in Python:")

print("""
1. int
2. float
3. complex
""")

print("Variables of numeric types are created when you assign a value to them:")

print("""
Example:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
""")

print("""
To verify the type of any object in Python, use the type() function:

Example:
print(type(x))
print(type(y))
print(type(z))
""")

#INTEGER
print('\n' + 10*'=', "int", 10*'=')

print("Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.")

print("""
Example

Integers:
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z)) 
""")

#FLOAT
print('\n' + 10*'=', "float", 10*'=')

print('Float, or "floating point number" is a number, positive or negative, containing one or more decimals.')

print("""
Example

Floats:
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
""")

print('Float can also be scientific numbers with an "e" to indicate the power of 10.')

print("""
Example

Floats:
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z)) 
"""
)

x = 35e3
y = 12E4
z = -87.7e100

print(x)
print(y)
print(z)

#COMPLEX
print('\n' + 10*'=', "complex", 10*'=')

print('Complex numbers are written with a "j" as the imaginary part:')

print("""
Example

Complex:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
""")

x = 3+5j
y = 5j
z = -5j

print(x)
print(y)
print(z)

#TYPE CONVERSION
print('\n' + 10*'=', "Type Conversion", 10*'=')

print("You can convert from one type to another with the int(), float(), and complex() methods:")

print("""
Example

Convert from one type to another:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
""")

x = 239 #integer
y = 34.9 #float
z = 34.5 #float
zz = 590 + 10j #complex

#convert
a = float(x)
b = int(y)
c = complex(z)
d = float(zz.real) #convert dari complex bilangan real ke float 
e = int(zz.imag) #convert dari bilangan imajiner ke int karena regulasi
f = complex(x) #convert dari int ke complex

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print("\n")

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

#RANDOM NUMBER
print('\n' + 10*'=', "Random Number", 10*'=')

print("""
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
""")
print("""
Example

Import the random module, and display a random number from 1 to 9:
import random

print(random.randrange(1, 10))
""")

#generate random number
import random #import modul random
print("result: ")
print(random.randrange(1, 100)) #generate angka random dari 1 sampai 100

print("""
 In our Random Module Reference you will learn more about the Random module.
 """)
