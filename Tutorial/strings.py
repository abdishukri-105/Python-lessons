#  Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#  or you can use three single quotes


#  Strings are Arrays

b = "Hello, World!"
print(b[4])

#  Looping Through a String

for h in "banana":
    print(h)


# String Length with len()

t  = "Hello, World!  "
print(len(t))

# Check String with keyword in 
txt = "The best things in life are free!"
print("free" in txt)

txt2 = "The best things in life are free!"
if "free" in txt2:
    print("Yes, 'free' is present.")

# Check if NOT

txt3 = "The best things in life are free!"
print("expensive" not in txt)

txt4 = "The best things in life are free!"
if "expensive" not in txt4:
      print("No, 'expensive' is NOT present.")



# slicing string 

k = "Hello, World!"
print(k[0:9])

l = "Hello, World!"
print(l[2:])  # Get the characters from position 2, and all the way to the end:

o = "Hello, World!"
print(o[-5:-2])   # Use negative indexes to start the slice from the end of the string:


    