a = 200
b = 33
if b > a:
  print("b is greater than a") #This indented region is known as a block of code
elif a == b:                   #thee block is what runs when the condition leading into it is true
  print("a and b are equal")
else:
  print("a is greater than b")


x = 33

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!") #This is a nested if, which means an if inside an if
  else:                         #All the indented code only runs when x>10 is true
    print("but not above 20.") 