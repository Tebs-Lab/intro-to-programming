# What does this function do?
def mystery_function(things, specific_thing):
    for thing in things:
        if specific_thing == thing:
            return True

    return False

# What will this print when executed?
return_value = mystery_function([1,2,3,4,5], 4)
print(return_value)

# What about this?
return_value = mystery_function([1,2,3,4,5], '4')
print(return_value)

# Run this code to check your answers.