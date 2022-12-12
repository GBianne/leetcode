# -*- coding: utf-8 -*-
"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

def orangesRotting(grid):
    
    # time
    minute = 0
    
    # early exit - no rotten orange
    if not any(2 in subgrid for subgrid in grid):
        if any(1 in subgrid for subgrid in grid):
            return -1
        else:
            return 0
        
    # failsafe - avoid endless loop
    nIter = 0    
    while nIter < len(grid)*len(grid[0]):        
        nIter += 1
        
        # check grid status
        # return if no fresh orange
        if not any(1 in subgrid for subgrid in grid):
            return minute
        else:
            minute += 1
            # propagated cells in this iter
            # storing into propCells instead of replacing to avoid messing with the loop below
            propCells = []
            # loop on grid
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 2:
                        # propagate to the right
                        if j+1 < len(grid[i]) and grid[i][j+1] == 1:
                            propCells.append((i,j+1))
                        # propagate to the left
                        if j-1 >= 0 and grid[i][j-1] == 1:
                            propCells.append((i,j+1))
                        # propagate to the top
                        if i+1 < len(grid) and grid[i+1][j] == 1:
                            propCells.append((i+1,j))
                        # propagate to the bottom
                        if i-1 >= 0 and grid[i-1][j] == 1:
                            propCells.append((i-1,j))
            # did we propagate something?
            if len(propCells) == 0:
                # no propagation - we already reached the end state
                # this is 100% a fail, since there were fresh oranges at the beginning of the iter
                return -1
            else:
                for (i,j) in propCells:
                    grid[i][j] = 2
            
            # go to next iteration

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))

print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))

print(orangesRotting([[0,2]]))