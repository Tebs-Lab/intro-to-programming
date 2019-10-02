"""
Complete this function such that it returns a new list
which contains all values that appear more than once in
the list passed into the function. Each duplicated value
should appear exactly once in the output list regardless
of how many times it is duplicated. 

If no items are duplicated, return an empty list.

This solution uses the "in" keyword, which returns true if 
the item is in the collection and also uses the "slice" syntax:

thing in collection --> returns True if thing is in collection. 
input_list[i+1:] --> returns a list with all the elements from index 
                     i+1 to the end of that list. 

Using these two features the solution checks if the current item occurs
in the list anywhere after the current item, then checks if that item
is not already in the return list. If both are true, it adds the current
item to the return list.
"""
def duplicates(input_list):
    return_list = []
    for i, item in enumerate(input_list):
        if item in input_list[i+1:] and item not in return_list:
            return_list.append(item)

    return return_list


# Very Simple Tests
# in Python == for two lists means "do the items in the list match exactly, order included"
assert duplicates([1, 2, 3, 1]) == [1]
assert duplicates([3, 3, 3, 3, 3]) == [3]

# Note the use of sorted here: your function can return the duplicates
# in any order, but calling sorted on them makes it easier to test the
# output. 
assert sorted(duplicates([1, 2, 3, 4, 1, 2, 3, 4])) == [1,2,3,4]
assert sorted(duplicates([1, 1, 2, 3, 3, 4])) == [1, 3]

## ADD AT LEAST 3 MORE TESTS ##
assert duplicates([1, 2, 3, 4, 5, 6]) == []
assert duplicates([1, 2, 3, 1, 5, 1]) == [1]
assert duplicates([1, 2, 3, 4, 6, 6]) == [6]

## Just helpful to see, if this prints your tests all passed!
print("All tests passed.")