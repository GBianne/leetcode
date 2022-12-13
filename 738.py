# -*- coding: utf-8 -*-
"""
An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.
"""

# simple but (extremely) inefficient algorithm:
# loop on k in range(n,0), check if k has MID, etc

# more efficient algorithm:
# split n into digits, loop on the digits and check MID condition, etc

# however, the problem is easily solved empirically:
# digit #1 of the solution (d0) has to be the minimum digit in n (* if no zero)
# then d0 is the minimum of nDigits
# and di is the minimum of nDigits[i:]
# the solution s is then [d0 d1 ... dk-1] where k is the number of digits of n

# example, n = 516358476
# nDigits = [5, 1, 6, 3, 5, 8, 4, 7, 6]
# d0 = min(nDigits) = 1
# d1 = min(nDigits[1:]) = 1
# d2 = min(nDigits[2:]) = 3
# d3 = min(nDigits[3:]) = 3
# d4 = min(nDigits[4:]) = 4
# d5 = min(nDigits[5:]) = 4
# d6 = min(nDigits[6:]) = 4
# d7 = min(nDigits[7:]) = 6
# d8 = min(nDigits[8:]) = 6
# and finally s = 113344466

# the 0-case
# the solution above is only valid if the digits of n do not contain any 0, else it would return zeros in front
# the highest MID would then be (k-1) occurrences of 9
# n = 100, s = 99
# n = 99990999, s = 9999999

def monotoneIncreasingDigits(n):
    
    # solution digits
    sDigits = []
    
    # 1 - split n into a list of digits
    nStr = str(n)
    nDigits = []
    for d in nStr:
        nDigits.append(int(d))
    
    # 2 - check for 0
    if 0 in nDigits:
        sDigits = ['9' for i in range(len(nDigits)-1)]
        s = int(''.join(sDigits))
        return(s)
        
    else:
        sDigits = [str(min(nDigits[k:])) for k in range(len(nDigits))]
        s = int(''.join(sDigits))
        return(s)
        
    
print(monotoneIncreasingDigits(516358476))
print(monotoneIncreasingDigits(516358076))