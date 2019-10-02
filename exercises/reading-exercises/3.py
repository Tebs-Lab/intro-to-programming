# What does this function do?
# How should we intepret its output (the variable return_value)
def mystery_function(input_string):
    return_value = {}

    for c in input_string:
        if return_value.get(c) == None:
            return_value[c] = 0
        
        return_value[c] += 1

    return return_value


# What will the following code result in?
# What does it mean?
some_string = 'This is a boring sentence.'
mystery_value = mystery_function(some_string)

print(mystery_value)