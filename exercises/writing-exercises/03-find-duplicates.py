"""
Complete this function such that it returns a new list
which contains all values that appear more than once in
the list passed into the function. Each duplicated value
should appear exactly once in the output list regardless
of how many times it is duplicated. 

If no items are duplicated, return an empty list. 
"""
def duplicates(input_list):
    # Delete pass, and put your code here.
    pass


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