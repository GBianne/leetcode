# -*- coding: utf-8 -*-
"""
You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.
"""

# straightforward

def getOrder(tasks):
    
    order = []
    availTasks = []
    
    # init time - the CPU stays idle until the first task kicks in
    time = min(task[0] for task in tasks)
    
    # failsafe mechanism after nTasks+1 iterations to avoid endless looping
    nIter = 0
    
    # main loop - continue until the order of all tasks is known or the failsafe is hit
    while (len(order) < len(tasks) and nIter < len(tasks)+1):
        nIter += 1
        
        # add to availTasks all tasks with enqueueTime <= time that werent already there or already processed
        for i in range (len(tasks)):
            if (not i in availTasks) and (not i in order) and (tasks[i][0] <= time):
                availTasks.append(i)
                
        # failsafe - availTasks empty
        # should never happen
        if len(availTasks) == 0:
            break
        
        # find the shortest task in availTasks
        shortestTask = -1
        for i in range(len(tasks)):
            if i in availTasks:
                if shortestTask == -1 or tasks[i][1] < tasks[shortestTask][1]:
                    shortestTask = i
                
        # compute the task
        order.append(shortestTask)
        availTasks.remove(shortestTask)
        
        # advance time
        time += tasks[shortestTask][1]
    
    return order

print(getOrder([[1,2],[2,4],[3,2],[4,1]]))

print(getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]]))