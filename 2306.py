# -*- coding: utf-8 -*-
"""
You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

Choose 2 distinct names from ideas, call them ideaA and ideaB.
Swap the first letters of ideaA and ideaB with each other.
If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.
"""

# hard? am i missing something?

def distinctNames(ideas):
    
    nValidNames = 0
    
    for idea1 in ideas:
        for idea2 in ideas:
            if idea1 != idea2:
                idea1Swapped = idea2[0] + idea1[1:]
                idea2Swapped = idea1[0] + idea2[1:]
                if (not idea1Swapped in ideas) and (not idea2Swapped in ideas):
                    nValidNames += 1
    
    return nValidNames

print(distinctNames(["coffee","donuts","time","toffee",]))

print(distinctNames(["lack","back"]))