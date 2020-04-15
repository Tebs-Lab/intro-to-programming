# We can create variables by giving them a name, and
# using the assignment operator, the equals sign (=)
# to give them a value.

# Data comes in a variety of types. These two versions
# of the number one are not the same. One is a number, 
# the other is a piece of text.
x = 1
y = '1'

# We can print the "type" of our two variables like this:
print('\n===quotes===')
print(type(x))
print(type(y))

# There are three kinds of numbers in python: integers, floats, and complex numbers
integer_example = 2
float_example = 0.1
complex_example = 4+3j # These are rarely important for most programmers... 

print('\n===number types===')
print(type(integer_example))
print(type(float_example))
print(type(complex_example))

# Booleans are either True or False
t = True
f = False

print('\n===booleans===')
print(type(t))
print(type(f))

# There is a special value that means "nothing"
nothing = None

print('\n===None===')
print(type(nothing))

# And textual data, called strings, are wrapped in quotes
text = "This is a string."
print(type(text))

# Micro-Exercise: Create a variable and assign it a value.
# Then, pick one of the variables defined above and reassign 
# it to have the same value as the variable you created.
# Finally, prove your code works with a print statement.
