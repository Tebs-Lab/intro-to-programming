"""
Complete this function such that it returns a list with
exactly two items. The first item should be the item that 
appears the MOST number of times in the provided input. 
The second item should be the item that occurs the fewest
number of times in the provided input.

The returned list can contain two of the same value, for example
if the input list has exactly one element, this would be the case.

If there are ties, e.g. input_list == [1, 1, 2, 2] your function
can select arbitrarily, that is the following would ALL be correct:
  [1, 1], [1, 2], [2, 1], [2, 2] 

If the input list is empty, return an empty list.
"""
def most_and_least_common(input_list):
    # Delete pass, and put your code here.
    pass


# Very Simple Tests
assert most_and_least_common([]) == []
assert most_and_least_common([1]) == [1, 1]
assert most_and_least_common([1,2,2]) == [2, 1]
assert most_and_least_common([1, 2, 1, 2, 3, 1, 2, 2]) == [2, 3]

## ADD AT LEAST 3 MORE TESTS ##
## How will you test for ties...?


## Just helpful to see, if this prints your tests all passed!
print("All tests passed.")