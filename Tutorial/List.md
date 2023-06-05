# List
Lists are used to store multiple items in a single variable.

From Python's perspective, lists are defined as objects with the data type 'list':

 > <class 'list'>


Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are **Tuple**, **Set**, and **Dictionary**, all with different qualities and usage.

Lists are created using square brackets:


> thislist = ["apple", "banana", "cherry"]
> print(thislist)
  

## List items

 - ordered
 - changeable 
 - allow duplicate values

 > List items are indexed, the first item has index [0], the second item has index [1] etc.

  ### Ordered
  When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

   If you add new items to a list, the new items will be placed at the end of the list.


   ### Changeable
   The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

  ### Allow Duplicates
  Since lists are indexed, lists can have items with the same value:


## List Items - Data Types  
List items can be of any data type and can contain many diff data types 
> list1 = ["abc", 34, True, 40, "male"]


## List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


 >  this is like map in js - produce new array that meets the condition

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:

``` 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
 for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
```

With list comprehension you can do all that with only one line of code:


```
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```


### the syntax
> newlist = [expression for item in iterable if condition == True]

The return value is a new list, leaving the old list unchanged.

### Condition

The condition is like a filter that only accepts the items that valuate to True.

> newlist = [x for x in fruits if x != "apple"]

The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

The condition is optional and can be omitted:

> newlist = [x for x in fruits]

### Iterable

The iterable can be any iterable object, like a list, tuple, set etc.

> newlist = [x for x in range(10)]

Same example, but with a condition:

> newlist = [x for x in range(10) if x < 5]

### Expression

The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

> newlist = [x.upper() for x in fruits]

You can set the outcome to whatever you like:

Set all values in the new list to 'hello':

> newlist = ['hello' for x in fruits]

The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

Return "orange" instead of "banana":

> newlist = [x if x != "banana" else "orange" for x in fruits]

The expression in the example above says:

"Return the item if it is not banana, if it is banana return orange".