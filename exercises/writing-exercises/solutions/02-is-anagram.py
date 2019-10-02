"""
Complete this function such that it returns True if and only if
the two strings passed to the function are anagrams of each other,
that is if they contain the same letters the same number of times.
Return False otherwise.

This solution loops through each string once and maintains a counter 
based on the characters it encounters. For the first string it increases
the count assoicated with that letter by one. For the second string it
decreases the count by one. 

If the counter object ends with counts of 0 for all characters, then 
the two strings must be anagrams. If any values are not 0 then the two
strings cannot be anagrams. The final loop performs this check. 
"""
def is_anagram(string_a, string_b):
    counter = {}

    for c in string_a:
        if counter.get(c) == None:
            counter[c] = 0
        
        counter[c] += 1

    for c in string_b:
        if counter.get(c) == None:
            counter[c] = 0
        
        counter[c] -= 1

    for c, count in counter.items():
        if count != 0:
            return False
    
    return True


# Very Simple Tests
assert is_anagram('abba', 'aabb') == True
assert is_anagram('aab', 'bba') == False
assert is_anagram('the detectives', 'detect thieves') == True
assert is_anagram('abcde', 'abcdf') == False
## ADD AT LEAST 3 MORE TESTS ##
assert is_anagram('abcde', 'ebcda') == True
assert is_anagram('AbA', 'aba') == False # Letters are case sensitive!
assert is_anagram('aaaa', 'aaaa') == True
assert is_anagram('aaaa', 'aaa') == False

## Just helpful to see, if this prints your tests all passed!
print("All tests passed.")