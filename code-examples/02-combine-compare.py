# Numbers can be combined using mathematical operators
x = 1 + 1
y = 2 * 3

# Variables holding numbers can be used any way numbers can be used
z = y / x

# We can prove that these computations worked out the same
# using comparison operators, specifically == to test for equality:
print('===comparing===')
print('2 == x', 2 == x)
print('6 == y', 6 == y)
print('3 == z', 3 == z)

print() # Just for a blank line in the output

# Two values can only be equal if they have the same type
print("1 == '1'", 1 == '1')

# Other common comparisons include <, <=, >, >=
print('1 < 2', 1 < 2)    # True
print('10 >= 10', 10 >= 10) # True
print('10 > 10', 10 > 10)  # False

print() # For a blank line in the output

# Strings are compared pseudoalphabetically for greater than / less than
print('"albert" < "bill"', "albert" < "bill") # True

# HOWEVER, in python ALL capital letters come before ANY lowercase letters
print('"B" < "a"', "B" < "a") # True

# There are additional rules for other characters like $, %, ., and so on
# that we're ignoring for now.

# Strings can also be combined with math operators, but they mean different
# things when operating on strings
x = "hello " + "world." # Concatination, x is "hello world."
y = "a" * 4 # Duplication, y = "aaaa"

print()
print(x)
print(y)

# Finally, we can combine the assignment operator and these math operations
# using the following shorthands:
x = 4
x + 3 #  x = x + 3
x -= 1 #  x = x - 1
x *= 2 #  x = x * 2
x /= 4 #  x = x / 4

# Micro-Exercise: predict the value of x. Then write a comparison statement 
# involving x that evaluates to False. Print the result of that comparison.
