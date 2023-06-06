
a = 33
b = 200
if b > a:
    print("b is greater than a")


# elif

c = 330
d = 33
if d > c:
  print("d is greater than c")
elif c == d:
  print("c and d are equal")
else:
    print("c is greater than d")




# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else
x = 330
y = 330
print("X") if x > y else print("Y")

# multiple if ... Else
print("X") if x > y else print("=") if x == y else print("Y")

# And

# The and keyword is a logical operator, and is used to combine conditional statements:

# Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


# OR 

# The or keyword is a logical operator, and is used to combine conditional statements:

# Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Not

# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


# Nested If

# You can have if statements inside if statements, this is called nested if statements.

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")