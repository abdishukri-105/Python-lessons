# loops

# while loop

i = 1 

while i < 6:
    # print(i)
    i += 1     




# the break statement
 
e = 1
while e < 6:
    # print(e)
    if e == 3:
        break
    e += 1 

# the continue statement

t = 0
while t < 6:
    t += 1
    if t == 3:
        continue
    print(t)



# The else Statement

# With the else statement we can run a block of code once when the condition no longer is true:

j = 1
while j < 6:
  print(j)
  j += 1
else:
  print("j is no longer less than 6")    