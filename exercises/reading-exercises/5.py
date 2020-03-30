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
    
    for item_a in list_a:
        if contains(list_b, item_a) and not contains(return_value, item_a):
            return_value.append(item_a)

    return return_value


# Setup two lists...
x = [1, 3, 5, 6, 7, 9, 1]
y = [3, 4, 5, 8, 10, 1]

# What will the following code print?
print(intersection(x, y))