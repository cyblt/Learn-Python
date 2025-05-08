#Python Variable

#Variable are containers for storing data values
"""
A variable is created the moment you first assign
a value to it.
"""
#example
x = 5
y = 3
print(x)
print(y)

#Variables do not need to be declared with any particular type. and can even change type after they have been set.
#example
x = 5
# x is of type int
x = "five"
# x is now of type str
print(x)


#Python Casting

#If you want to specify the data type of a variable, this can be done with casting.
#example
x = str(3) # x will be "3"
x = int(3) # x will be 3
x = float(3) # x will be 3.0
print(x)

#Get the Type (cara mengetahui tipe data)
y = "stringg"
z = 3.0
print(type(y))
print(type(z))

#Single or Double Quotes?
print(5*'=', "Single or Double Quotes?", 5*'=')
#String variables can be declared either by using single or double quotes
#example
xx = "John"
yy = 'John'
#Bisa salah satu
print(xx)


#Case-Sensitive
print(5*'=', "Case-Sensitive", 5*'=')
