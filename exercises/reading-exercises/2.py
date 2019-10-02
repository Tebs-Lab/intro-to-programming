# What does this function do?
def mystery_function(names):
    counter = 0

    for name in names:
        if name[0] == 'A':
            counter += 1
        elif name[-1] == 'z':
            counter += 1
    
    return counter


# How is this function different from the one above it?
def mystery_function_two(names):
    counter = 0

    for name in names:
        if name[0] == 'A':
            counter += 1
        if name[-1] == 'z':
            counter += 1
    
    return counter


# Test your understanding of the above functions by predicting their output
# with the following input.
student_names = [
    'Tyler',
    'Taz',
    'Amanda',
    'Zeke',
    'Adnan',
    'Amoz',
    'Frank'
]

return_one = mystery_function(student_names)
return_two = mystery_function_two(student_names)

# What will these prints
print(return_one)
print(return_two)