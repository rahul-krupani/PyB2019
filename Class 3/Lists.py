# A list is a sequence of values. They are mutable
# They are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish.

# Syntax of list functions:

# list.append(object)
# list.count(object)
# list.extend(iterable)
# list.index(object, start, stop)
# list.pop(index) Default pops the last element
# list.remove(object)
# list.reverse()
# list.sort([reverse=True]) True implies descending order

# list = list.copy()
# Directly doing list = list means both the lists refers to the same memory space

#Simple appending in lists
print("Appending and iterating through list:\n")
mylist = []
mylist.append(1)
mylist.append("Hi")
mylist.append(6.9)
print("list[0]:", mylist[0]) # prints 1
print("list[1]:", mylist[1]) # prints "Hi"
print("list[2]:", mylist[2]) # prints 6.9

# iterate through a list
print("\nList is:")
for item in mylist:
    print(item,end =" ")
print("\n"*2)
#More functions using lists:

exampleString = "Sphinx of black quartz judge my vow"
exampleString = exampleString.lower()

# Converting a string to list gives a list of all characters
print("List is:")
alphabets = list(exampleString)
print(alphabets, len(alphabets), "\n")

# Converting a list to set object removes all duplicates
# Sets have the same functions as lists but without duplicates
print("Convert from list to set")
alphabets = set(alphabets)
print(alphabets, len(alphabets), "\n")

# Removing space from the list to obtain a list of alphabets
print("Remove space")
alphabets.remove(' ')
print(alphabets, len(alphabets), "\n")
alphabets = list(alphabets)

# Sorting the list in alphabetical order
print("list.sort()")
alphabets.sort()
print(alphabets, len(alphabets), "\n")

#NOTE:The default sort in python proves to be much faster than the usual bubble sort algorithm especially over large test cases

# Pop without an index removes the last object in the list
print("list.pop()", alphabets.pop())
print(alphabets, len(alphabets), "\n")

# Append adds an object to the end of the list
print("list.append()", alphabets.append('z'))
print(alphabets, len(alphabets), "\n")

# Reverse just reverses the list
print("list.reverse()")
alphabets.reverse()
print(alphabets, len(alphabets), "\n")

# Clear makes it an empty list
print("list.clear()")
alphabets.clear()
print(alphabets, len(alphabets), "\n")

# Slicing a list
print("list[start:end:step]")
print(alphabets[:20:2], "\n")

