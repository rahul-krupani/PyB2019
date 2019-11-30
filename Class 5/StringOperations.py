#Python offers a variety of functions to manipulate strings according to our need
 
exampleString = "Sphinx of black quartz, judge my vow."

print(exampleString, len(exampleString))
exampleString = exampleString.title()
print("str.title()", exampleString)
# Similarly str.upper(), str.lower(), str.swapcase(), str.capitalize()

#count occurences of a character
print("str.count('character')", exampleString.count('a'))
#slice a string
print("str[start:end:step]", exampleString[3:25])
#NOTE:This method slicing can be applies to lists also in a similar fashion and is widely used

exampleString = "..Sphinx of black quartz,,, judge my vow."
print("\n", exampleString)
# removes chars at the right end of the string
print("str.rstrip(chars)", exampleString.rstrip('.'))
# removes chars at the left end of the string
print("str.lstrip(chars)", exampleString.lstrip('.'))
# removes chars at the both ends of the string
print("str.strip(chars)", exampleString.strip('.'), "\n")

# Returns an Integer
print("str.count(chars, __start, __end)", exampleString.count('.'), "\n")

exampleString = "Sphinx of black quartz, judge my vow."
print(exampleString)
# Returns a Bool
print("str.startswith(prefix, start, end)", exampleString.startswith("Sph"))
print("str.endswith(suffix, start, end)", (exampleString.endswith("vow")), "\n")
print("str.replace(old, new, count)", exampleString.replace(',', ''), "\n")

# ValueError if not found
print("str.index(sub, __start, __end)", exampleString.index('h'))

# Returns -1 if not found
print("str.find(sub, __start, __end)", exampleString.find(';'), "\n")

# Returns a Bool
# str.isalnum() str.isalpha() str.isdecimal() str.isdigit() str.isidentifier()
# str.islower() str.isnumeric() str.isprintable() str.isspace() str.istitle() str.isupper()

# Returns a List
print("str.split(sep, maxsplit)", exampleString.split(" ", 2), sep="\n")

# str.join() is a flexible way of concatenating strings
randomString="-"
print("\nanother_str.join(str)", randomString.join(exampleString))
