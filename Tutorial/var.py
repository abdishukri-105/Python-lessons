

# A variable is created the moment you first assign a value to it.

x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

z = 4       # x is of type int
z = "Sally" # x is now of type str
print(z)

# casting
# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get the Type
# You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))

# Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"

#  One Value to Multiple Variables

x = y = z = "Orange"

#  Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a, b, c)


