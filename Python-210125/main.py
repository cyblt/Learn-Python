print(10*'=', "Python Var pt.3 Assign Multiple Values", 10*'=', "\n")

print(10*'=', "Many Values to Multiple Variables", 10*'=')
# Python allows you to assign values to multiple variables in one line:

x, y, z = "aku", "bukan", "cicak"
print(x, y, z)
print(x)
print(y)
print(z)

# Note: Make sure the number of variables matches the number of values, or else you will get an error.

print(10*'=', "One Value to Multiple Variables", 10*'=')
# And you can assign the same value to multiple variables in one line:

k = l = m = "satu value multi variable"
print(k)
print(l)
print(m)


print(10*'=', "Unpack a Collection", 10*'=')
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["banana", "grape", "guava"]
a, b, c = fruits

print(a)
print(b)
print(c)

