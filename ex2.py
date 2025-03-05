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

    # copied from lab 3 implementations
    def merge_sort(self, arr):

        if(len(arr) <= 1):
            return arr

        mid = len(arr) // 2
        


    # copied from lab 3 implementations
    def merge(self, low, mid, high):
        left = self[low:mid+1]           # left half of the array
        right = self[mid+1:high+1]       # right half of the array

        # pointers to use
        i = 0
        j = 0
        k = low 

        while(i < len(left) and j < len(right)):
            # compare the elements from both arrays
            if(left[i] <= right[j]):
                self[k] = left[i]
                i+=1
            else:
                self[k] = right[j]
                j+=1
            k+=1

        # copy any remaining elements from left array
        while(i < len(left)):
            self[k] = left[i]
            i+=1
            k+=1

        # copy any remaining elements from right array
        while(i < len(right)):
            self[k] = right[j]
            j+=1
            k+=1
        

