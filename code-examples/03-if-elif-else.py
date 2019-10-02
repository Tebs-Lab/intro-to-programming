x = 7
# We use if, if/else, and if/elif/else blocks to selectively
# execute code when something is true.

if True:
    print("This executes")

if False: 
    print("This never executes")


# The above are trivial, but using comparison operators makes
# these constructs very useful:

arbitrary_number = 42

# Only ONE of an if/else block can trigger.
if arbitrary_number > 10:
    print("The number is larger than 10")
else:
    print("The number is not larger than 10")

# Same for an if/elif/else, exactly one block can trigger.
# But you can have any number of elifs
if arbitrary_number < 10:
    print("The number is less than 10")
elif arbitrary_number < 20:
    print("The number is between 10 and 20")
elif arbitrary_number < 30:
    print("The number is between 20 and 30")
else:
    print("The number is 30 or larger")

# comparisions can be combined using and / or
# they can also be negated with not
if not arbitrary_number > 10:
    print("The number is NOT greater than 10.")

if arbitrary_number > 10 and arbitrary_number < 50:
    print("The number is greater than 10 AND less than 50")

if arbitrary_number < 10 or arbitrary_number > 30:
    print("The number is less than 10, or more than 30")