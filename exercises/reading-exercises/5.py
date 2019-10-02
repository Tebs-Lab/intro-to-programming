# This code has better names, but does something we haven't seen before:
# It calls a function from within another function.

# Can you describe how these functions work together, and what the ultimate
# result of this code is?

def contains(items, item):
    for i in items:
        if item == i:
            return True
    
    return False


def intersection(list_a, list_b):
    return_value = []
    
    for outer_item in list_a:
        if contains(list_b, outer_item) and not contains(return_value, outer_item):
            return_value.append(outer_item)

    return return_value


# What will the following code print?
a = [1, 3, 5, 6, 7, 9]
b = [3, 4, 5, 8, 10, 1]

print(intersection(a, b))