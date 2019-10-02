# Numbers can be combined using mathematical operators
two = 1 + 1
six = 2 * 3

# Variables holding numbers can be used the same way
three = six / two

# The names of these variables is not understood or considered
# by the computer. Naming two, six, and three differently does
# not change the behavior of the above code. But it is harder 
# to read by a human:
x = 1 + 1
y = 2 * 3
z = y / x

# We can prove that these computations worked out the same
# using comparison operators, specifically == to test for 
# equality:
print('===comparing===')
print(two == x)
print(six == y)
print(three == z)

print() # Just for a blank line in the output

# Two values can only be equal if they have the same type
print("1 == '1'", 1 == '1')

# Other common comparisons include <, <=, >, >=
1 < 2    # True
10 >= 10 # True
10 > 10  # False

# Strings are compared pseudoalphabetically for greater than / less than
"albert" < "bill" # True

# HOWEVER, in python ALL capital letters come before ANY lowercase letters
"B" < "a" # True

# There are additional rules for other characters like $, %, ., and so on
# that we're ignoring for now.

# Strings can also be combined with math operators, but they mean different
# things when operating on strings
x = "hello " + "world." # Concatination, x is "hello world."
y = "a" * 4 # Duplication, y = "aaaa"

# Finally, we can combine the assignment operator and these math operations
# using the following shorthands:

x += 1 #  x = x + 1
x -= 1 #  x = x - 1
x *= 1 #  x = x * 1
x /= 1 #  x = x / 1