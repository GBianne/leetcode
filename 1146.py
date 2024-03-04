# -*- coding: utf-8 -*-
"""
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
"""

class SnapshotArray(object):
    
    # the initial array is [ [0], [0], ..., [0]]
    # everytime a snapshot is done, a new value is pushed to every sub-list
    # any call to set() will modify the latest value only
    # get() will return the snap_id-th element of the index-th element
    
    def __init__(self, length):
        # init snap_id to -1, as there is no snapshot initially
        self.snap_id = -1
        if length > 0:
            self.array = [[0] for k in range(length)]
        else:
            print("Init error - invalid length")
            self.array = []
    
    def set(self, index, val):
        if index >= 0 and index < len(self.array):
            self.array[index][-1] = val
        else:
            print("Set error - index out of bounds")
    
    def snap(self):
        # add a new entry to every sublist, value equal to the current one
        for k in range(len(self.array)):
            self.array[k].append(self.array[k][-1])
        # increment the snap_id
        self.snap_id += 1
        print("Snapshot taken! snap_id is now", self.snap_id)
        return self.snap_id
    
    def get(self, index, snap_id):
        if index >= 0 and index < len(self.array):
            if snap_id >= 0 and snap_id < len(self.array[index]):
                return self.array[index][snap_id]
            else:
                print("Get error - snap_id out of bounds")
                return
        else:
            print("Get error - index out of bounds")
            return

snapshot_arr = SnapshotArray(3)
snapshot_arr.set(0,5)
snapshot_arr.snap()
snapshot_arr.set(0,6)
print(snapshot_arr.get(0,0))
snapshot_arr.set(2,2)
snapshot_arr.snap()
snapshot_arr.set(1,4)
print(snapshot_arr.get(0,1))
print(snapshot_arr.get(1,1))
print(snapshot_arr.get(1,2))