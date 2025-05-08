# Python Casting
print(10*'=', "Python Casting", 10*'=')

print("Specify a Variable Type")

print("""
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
""")

print("""
Mungkin ada saatnya Anda ingin menentukan tipe pada variabel. Ini dapat dilakukan dengan casting. Python adalah bahasa berorientasi objek, dan karenanya menggunakan kelas untuk menentukan tipe data, termasuk tipe primitifnya.
""")

print("Casting in python is therefore done using constructor functions:\n")

print("Oleh karena itu, casting dalam python dilakukan dengan menggunakan fungsi konstruktor:")

print("""
int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
""")

print("""
int() - membuat bilangan integer dari literal integer, literal float (dengan menghapus semua desimal), atau literal string (dengan syarat string tersebut mewakili bilangan bulat)
float() - membuat bilangan float dari literal integer, literal float, atau literal string (dengan syarat string tersebut mewakili float atau integer)
str() - membuat string dari berbagai macam tipe data, termasuk string, literal integer, dan literal float
""")

print("""
Example

Integers:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
""")

print("""
Example

Floats:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
""")

print("""
Example

Strings:
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
""")