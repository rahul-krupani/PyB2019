# Tuples are a sequence of values. They are Immutable.
# Tuples are work faster than lists.
# Hence are used in places where objects need to be immutable like dictionaries

# Syntax of tuple functions
example_tuple = tuple([i for i in range(10)])
print(example_tuple)

# integer = tuple.index(x, start, stop)
print("tuple.index(value, start, stop) ", example_tuple.index(7))

# integer = tuple.count(object)
example_tuple = (1, 1, 1)
# This is a redeclaration, tuple is still not mutable
print("tuple.count() ", example_tuple.count(1))
