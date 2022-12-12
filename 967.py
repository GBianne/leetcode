# -*- coding: utf-8 -*-
"""
Given two integers n and k, return an array of all the integers of length n where the difference between every two consecutive digits is k. You may return the answer in any order.

Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.
"""

# straightforward with a binary tree, but python does not have built-in trees
# non-tree algorithm:
# - create a dict where a digit d in [0,9] is linked to up to two next digits d+k and d-k (if in [0,9])
# - loop on n using the dict to output all numbers

def numsSameConsecDiff(n, k):
    
    # digit linking dict
    digitLink = dict()
    for d in range(10):
        digitLink[d] = []
        if d-k >= 0:
            digitLink[d].append(d-k)
        if d+k <= 9 and k > 0:
            # do not append twice if k = 0
            digitLink[d].append(d+k)
            
    solution = []
    
    for d1 in range(1,10):
        if len(digitLink[d1]) > 0:
            solution.append(d1)
    # all possible first digits are now here
    # now at every stage, loop on solution and add the other available paths
    for silentIter in range(1,n):
        lenSol = len(solution)
        # the solution list will be changed inside the loop, hence lenSol
        for j in range(lenSol):
            # get the last digit of solution[j]
            lastDigit = int(str(solution[j])[-1])
            # see where we can go from there
            # only two options:
            # 1 - digitLink links to one other digit
            #   -> append that digit to the solution
            # 2 - digitLink links to two other digits
            #   -> copy the solution, and append one of the digits to each
            # no possibility of accessing a digit without links
            if len(digitLink[lastDigit]) == 1:
                # modify solution[j] to add the next digit
                solution[j] = int(str(solution[j])[:-1] + str(lastDigit) + str(digitLink[lastDigit][0]))
            elif len(digitLink[lastDigit]) == 2:
                # two ways to go from there, d+k (posSol) and d-k (negSol)
                # d-k (negSol) is first in the dict
                negSol = int(str(solution[j])[:-1] + str(lastDigit) + str(digitLink[lastDigit][0]))
                posSol = int(str(solution[j])[:-1] + str(lastDigit) + str(digitLink[lastDigit][1]))
                # replace solution[j] with one
                solution[j] = negSol
                # and append the other
                solution.append(posSol)
            else:
                # cannot happen
                print("error code 1 - ?!")
                return([])
        
    solution.sort()
    
    return solution

print(numsSameConsecDiff(3,7))

print(numsSameConsecDiff(2,1))

print(numsSameConsecDiff(5,1))