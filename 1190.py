# -*- coding: utf-8 -*-
"""
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.
"""

# idea: loop through the string with an indentation index
# every ( increases the current indentation level by 1 and shifts to a new substring
# every ) decreases the current indentation level by 1, reverses the current substring and appends it to the previous one
# every other char gets appended to the current substring
# since the parentheses are guaranteed to be balanced, the end of the string will have indentation back to 0

def reverse_parentheses(s):
    
    # current indentation level - start from 0
    ind_level = 0
    
    # current storage - list of substrings, every indentation level adds a dimension
    storage = ['']
    
    for char in s:
        if char == '(':
            # see line 11
            ind_level += 1
            storage.append('')
        elif char == ')':
            # see line 12
            ind_level -= 1
            storage[-2] += storage[-1][::-1] # storage[-2] will never get out of bounds since ) can only happen after (
            storage.pop()
        else:
            # see line 13
            storage[-1] += char
            
    # catching potential errors - see line 14
    if len(storage) != 1:
        print("Error - final indentation level is not 0")
        return ''
    
    return storage[0]

print(reverse_parentheses("(abcd)"))
print(reverse_parentheses("(u(love)i)"))
print(reverse_parentheses("(ed(et(oc))el)"))