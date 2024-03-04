# -*- coding: utf-8 -*-
"""
You are given a large sample of integers in the range [0, 255]. Since the sample is so large, it is represented by an array count where count[k] is the number of times that k appears in the sample.

Calculate the following statistics:

minimum: The minimum element in the sample.
maximum: The maximum element in the sample.
mean: The average of the sample, calculated as the total sum of all elements divided by the total number of elements.
median:
If the sample has an odd number of elements, then the median is the middle element once the sample is sorted.
If the sample has an even number of elements, then the median is the average of the two middle elements once the sample is sorted.
mode: The number that appears the most in the sample. It is guaranteed to be unique.
Return the statistics of the sample as an array of floating-point numbers [minimum, maximum, mean, median, mode]. Answers within 10-5 of the actual answer will be accepted.
"""

import random

# minimum: start from the first index, stop at the first non-zero entry
def minimum(array):    
    for k in range(len(array)):
        if array[k] > 0:
            return k    
    # default return - empty array
    return -1

# maximum: start from the last index, stop at the first non-zero entry
def maximum(array):    
    for k in reversed(range(len(array))):
        if array[k] > 0:
            return k    
    # default return - empty array
    return -1

# elt_count: local function computing the element count
def elt_count(array):    
    count = 0
    for k in range(minimum(array), maximum(array)+1):
        count += array[k]
    return count

# mean: compute in range [min, max]
def mean(array):
    mean_val = 0
    n_elt = elt_count(array)
    for k in range(minimum(array), maximum(array)+1):
        mean_val += k*array[k]/float(n_elt)
    return mean_val

# median: compute in range [min, max]
def median(array):
    n_elt = elt_count(array)
    # even or odd count?
    if (n_elt % 2) == 0:
        # the median count is between n_elt/2 and (n_elt/2)+1
        med = -1 # provisional median storage if two different values
        seen = 0 # amount of elements seen while looping
        for k in range(minimum(array), maximum(array)+1):
            seen += array[k]
            if seen == n_elt/2 and array[k] > 0:
                # the median is the average between this and the next element - store for now
                med = k
            elif seen > n_elt/2:
                # 1 - we havent triggered the if before - both indexes have the same value
                if med == -1:
                    return k
                # 2 - we have triggered the if before - two different values
                else:
                    return (med+k)/2.
        return -1
    else:
        # the median count is the ceiling of n_elt/2. - integer division + 1
        seen = 0 # amount of elements seen while looping
        for k in range(minimum(array), maximum(array)+1):
            seen += array[k]
            if seen >= (n_elt/2)+1:
                return k
        return -1

# mode: loop in range [min, max] - the mode is guaranteed to be unique
def mode(array):
    cur_mode = 0 # current mode as we loop through
    for k in range(minimum(array), maximum(array)+1):
        if array[k] > array[cur_mode]:
            cur_mode = k
    return cur_mode

# main function
def get_stats(array):
    stats = []
    # rounding to 10^-5
    stats.append(round(float(minimum(array)),5))
    stats.append(round(float(maximum(array)),5))
    stats.append(round(float(mean(array)),5))
    stats.append(round(float(median(array)),5))
    stats.append(round(float(mode(array)),5))
    return stats

#count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#count = [0,1,5,4,1,2,0,2,1,2,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
count = [random.randint(0,10) for k in range(256)]

print(get_stats(count))