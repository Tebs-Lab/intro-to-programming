"""
Complete this function such that it returns True if and only if
the string passed into this function is a palindrome, that is if 
it is the same string of characters forwards and in reverse. 
Return False otherwise. 

This solution computes the midpoint of the input_string and then
compares letters from the outside in, one by one, until it gets 
to the two center.

len(input_string) // 2  --> divides by two, then rounds down.
range(any_number) --> returns an iterator with integers from 0 to (any_number - 1)
""" 
def is_palindrome(input_string):
    front = 0
    back = -1
    for _ in range(len(input_string) // 2):
        if input_string[front] != input_string[back]:
            return False
        
        front += 1
        back -= 1
    
    return True


# Very Simple Tests:
assert is_palindrome('racecar') == True
assert is_palindrome('battle') == False
assert is_palindrome('wasitabatisaw') == True
assert is_palindrome('a') == True
assert is_palindrome('abca') == False
## ADD AT LEAST 3 MORE TESTS ##
assert is_palindrome('') == True
assert is_palindrome('aa') == True
assert is_palindrome('ab') == False
assert is_palindrome('aba') == True
assert is_palindrome('abb') == False


## Just helpful to see, if this prints your tests all passed!
print("All tests passed.")