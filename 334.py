# -*- coding: utf-8 -*-
"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""

# naive algorithm: loop on nums, store nums[i], loop on nums[i+1:] to find nums[j] > nums [i], loop on nums[j+1:] etc
# terribly inefficient

# other idea: we dont care about finding a specific occurrence, we just want to know if there is at least one ITS or not
# - store three ints a, b and c initialised at nums[0,1,2].
# - loop on nums[3:], trying to find (a,b,c) such that a < b < c
# - the state of (a,b,c) is then evaluated at the beginning of the loop in order to set an action
# 1. a = max(a,b,c)
#   => a is irrelevant and can be erased. any new value will be pushed to the right, (a,b,c) <- (b,c,new). action = push
# 2. b = max(a,b,c)
#   a. a < c
#     => b is irrelevant and can be switched with c, then replaced. (a,b,c) <- (a,c,new). action = dance
#   b. a >= c
#     => if new <= c, then c is irrelevant and can be replaced.(a,b,c) <- (a,b,new). action = replace
#        if new > c, then only the lower sequence out of (a,b) and(c,new) will be kept
#          -> if b <= new, there isnt a point in storing it. action = skip
#   	   -> if b > new, (c,new) becomes the new preferred sequence. action = push
#        action = unknown, then decide based on new
# 3. c = max(a,b,c)
#   a. a < b
#       => since c is the max and b isn't, then we have a < b < c. return true!
#   b. a >= b
#       => a is irrelevant. action = push
# - continue until the end of the list is reached, then return false

# there might be (is probably) a clearer algorithm, but i like this :)

# time complexity is O(n), the list is only gone through once with an O(1) amount of operations in each loop
# space complexity is O(1), only three integers and one string are stored regardless of nums length

def increasingTriplet(nums):
    
    # dummy fail
    if len(nums) < 3:
        return False
    else:
        a = nums[0]
        b = nums[1]
        c = nums[2]
    
    # initialise action
    action = "unknown"
    
    # loop on nums
    for new in nums[3:]:
        
        # evaluate the state of (a,b,c)
        if a == max(a,b,c):
            action = "push"
        elif b == max(a,b,c):
            if a < c:
                action = "dance"
            else:
                action = "unknown"
        else:
            if a < b:
                # yay - note: this will only be reached if the initial subsequence is ITS
                return True
            else:
                action = "push"
        
        # unknown action? decide by comparing the new value to c and b
        if action == "unknown":
            if new <= c:
                action = "replace"
            else:
                if new >= b:
                    action = "skip"
                else:
                    action = "push"
        
        # switch on action
        if action == "replace":
            c = new
        elif action == "push":
            a = b
            b = c
            c = new
        elif action == "dance":
            b = c
            c = new
        # else skip
        
        # end of loop check
        if a < b < c:
            return True
    
    return False

print(increasingTriplet([1,2,3,4,5]))

print(increasingTriplet([5,4,3,2,1]))

print(increasingTriplet([2,1,5,0,4,6]))

print(increasingTriplet([5,1,7,3,4]))