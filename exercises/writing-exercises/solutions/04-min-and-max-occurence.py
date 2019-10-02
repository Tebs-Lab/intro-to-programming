"""
Complete this function such that it returns a list with
exactly two items. The first item should be the item that 
appears the MOST number of times in the provided input. 
The second item should be the item that occurs the FEWEST
number of times in the provided input.

The returned list can contain two of the same value, for example
if the input list has exactly one element, this would be the case.

If there are ties, e.g. input_list == [1, 1, 2, 2] your function
can select arbitrarily, that is the following would ALL be correct:
  [1, 1], [1, 2], [2, 1], [2, 2] 

If the input list is empty, return an empty list.
"""
def most_and_least_common(input_list):
    # To handle the requirement of returning an empty list
    # for an empty input list. 
    if len(input_list) == 0:
        return []

    counter = {}
    for item in input_list:
        if counter.get(item) == None:
            counter[item] = 0
        
        counter[item] += 1
    
    # These values are chosen to be impossible so that 
    # the time through the following loop, the initial 
    # comparisons will always be True
    min_count = len(input_list) + 1
    min_value = None

    max_count = 0
    max_value = None
    print(counter)
    for item, count in counter.items():
        if count < min_count:
            min_count = count
            min_value = item

        if count > max_count:
            max_count = count
            max_value = item

    return [max_value, min_value]



# Very Simple Tests
assert most_and_least_common([]) == []
assert most_and_least_common([1]) == [1, 1]
assert most_and_least_common([1,2,2]) == [2, 1]
assert most_and_least_common([1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]) == [1, 5]

## ADD AT LEAST 3 MORE TESTS ##
print(most_and_least_common([1, 2, 1, 2, 3, 1, 2, 2]))
assert most_and_least_common([1, 2, 1, 2, 3, 1, 2, 2]) == [2, 3]

## Unfortunately, it's not as easy to test for ties, but here is one way in 3 lines:
computed_answer = most_and_least_common([1, 1, 2, 2])
assert computed_answer[0] in [1, 2]
assert computed_answer[1] in [1 ,2]

# Another test for ties, one most but a tie for least
computed_answer = most_and_least_common([1, 1, 1, 2, 2, 3, 3, 4, 4])
assert computed_answer[0] == 1
assert computed_answer[1] in [2 ,3, 4]


## Just helpful to see, if this prints your tests all passed!
print("All tests passed.")