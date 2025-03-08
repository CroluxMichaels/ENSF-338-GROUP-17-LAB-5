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


# Q2
class PriorityQueueInsert:
    """Priority queue implementation by maintaining a sorted list."""
    
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        """Insert the value in the correct sorted position."""
        if not self.queue:
            self.queue.append(value)
        else:
            for i in range(len(self.queue)):
                if self.queue[i] > value:
                    self.queue.insert(i, value)
                    return
            self.queue.append(value)
    
    def dequeue(self):
        """Remove and return the first element, or None if empty."""
        if self.queue:
            return self.queue.pop(0)
        return None

# Q3
def generate_tasks(n=1000, enqueue_prob=0.7):
    """Generate a list of tasks where enqueue has a probability of 0.7."""
    tasks = []
    for _ in range(n):
        if random.random() < enqueue_prob:
            tasks.append(("enqueue", random.randint(1, 1000)))
        else:
            tasks.append(("dequeue", None))
    return tasks


def run_tasks(queue_class, tasks):
    """Execute tasks on the given priority queue class."""
    pq = queue_class()
    for action, value in tasks:
        if action == "enqueue":
            pq.enqueue(value)
        else:
            pq.dequeue()


# Q4
tasks_list = [generate_tasks() for _ in range(100)]

time_sorted = timeit.timeit(lambda: [run_tasks(PriorityQueueSorted, tasks) for tasks in tasks_list], number=1)
time_insert = timeit.timeit(lambda: [run_tasks(PriorityQueueInsert, tasks) for tasks in tasks_list], number=1)

print(f"Time taken by PriorityQueueSorted: {time_sorted:.6f} seconds")
print(f"Time taken by PriorityQueueInsert: {time_insert:.6f} seconds")


# Q5
"""
The PriorityQueueInsert implementation is expected to be faster than PriorityQueueSorted.
The reason is that PriorityQueueSorted appends the value and then sorts the whole list using merge sort (O(n log n)),
whereas PriorityQueueInsert keeps the list sorted by inserting in the correct place (O(n) worst case).

For large inputs, repeated sorting in PriorityQueueSorted becomes inefficient compared to inserting in the correct place.
Therfore, maintaining a sorted list via insertion is the better approach in this case.
"""