'''
syntax of output 
print(values = '', sep=' ', end='\n')
'''

print("A", "B", "Notice the Space")
print("This", "Is", "In", "A", "New", "Line", sep="_")
print("Hello", end="")
print("World.\n")

'''
syntax of input
variable = input(prompt='')
'''

x = input("Enter any number: ")
print(x, " is of type ", type(x)) #always returns a string
