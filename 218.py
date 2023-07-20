# -*- coding: utf-8 -*-
"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.
"""

# important note: the buildings entries are sorted in non-decreasing left order
# objective: build the skyline point after point to write values only once, and only append to the skyline
# possible algorithms:
# 1. loop over the buildings -> need to insert and re-write the skyline all the time
# 2. loop over the heights -> wont be in ascending x order, same issue
# 3. loop over x -> looks fine!
# let's go over x, building the skyline point by point

def getSkyline(buildings):
    
    skyline = []
    
    # loop over x
    x = -1
    # stop condition reached when x is greater than the last left entry
    stop = False
    # current skyline height
    skyHeight = 0
    
    while not stop:
        
        # increment x
        x += 1        
        # reset the new height
        newHeight = 0
        # did we find a building for this value of x?
        found = False
        # did we break the buildings loop for this value of x?
        broke = False
    
        # check if there is a building for this value of x
        for entry in buildings:
            if entry[0] > x:
                # buildings are in non-decreasing left order
                # we are done checking relevant buildings, but there are more to come
                broke = True
                break
            elif entry[1] > x:
                # the current entry spans over x
                found = True
                # check this building entry against newHeight
                if entry[2] > newHeight:
                    # this building is higher! update the new height
                    newHeight = entry[2]
        # done checking the buildings for this value of x - did we find anything?
        if found:
            if newHeight != skyHeight:
                skyline.append([x, newHeight])
            skyHeight = newHeight
        else:
            # a-ha! no building spans across this value of x
            # was the skyline height already 0? else, we need to append this point
            if skyHeight != 0:
                skyline.append([x,0])
                skyHeight = 0
            # are we done? if we reached the end of the buildings loop without broke or found = True, we are!
            if not broke:
                stop = True
        
    return skyline

print(getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
print(getSkyline([[0,2,3],[2,5,3]]))
print(getSkyline([[1,5,7],[3,4,15],[6,17,10],[6,15,11],[8,45,4],[12,32,8],[21,23,5],[21,23,22],[31,39,14],[32,36,15],[33,36,19],[41,44,20],[43,47,5],[55,65,42]]))