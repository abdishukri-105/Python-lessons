#  Lists

mylist = ["apple", "banana", "cherry"]

#  List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
# print(newlist)

# with list compression

newlist = [x for x in fruits if "a" in x]    
#  this is like map in js  -  produce new array that meets the condition