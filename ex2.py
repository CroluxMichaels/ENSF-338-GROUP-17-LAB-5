import timeit
import random

# Q1
class PriorityQueueSorted:
    """Implementation after each enqueue"""
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        """Insert element then do merge sort"""
        self.queue.append(value)
        # merge sort to be implemented here


    def dequeue(self):
        """Remove and return first element, if empty then return nothing"""
        if(self.queue):
            return self.queue.pop(0)
        
        return None


    def merge_sort(self, arr):

        if(len(arr) <= 1):
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)


    def merge(self, left, right):

        result = [] 

        i = j = 0

        while (i < len(left) and j < len(right)):
            if(left[i] < right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # append elements 
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result

