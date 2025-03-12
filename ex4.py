import timeit
import random
import matplotlib.pyplot as plt

# Question 1
class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)  

    def dequeue(self):
        if len(self.queue) == 0:
            return None  # Queue is empty
        return self.queue.pop() 

# Question 2
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.head:  # If queue is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if not self.head:
            return None  # Queue is empty

        # If only one node exists
        if self.head == self.tail:
            data = self.head.data
            self.head = self.tail = None
            return data

        # Find second-to-last node
        current = self.head
        while current.next and current.next != self.tail:
            current = current.next

        # Remove the tail node
        data = self.tail.data
        current.next = None
        self.tail = current 
        return data

# Question 3
def generate_random_tasks(num_tasks=10000):
    task_list = []
    enqueue_no, dequeue_no = 0, 0

    for _ in range(num_tasks):
        should_dequeue = random.random() < 0.3 and enqueue_no > dequeue_no

        if should_dequeue:
            task_list.append("dequeue") 
            dequeue_no += 1
        else:
            task_list.append("enqueue")  
            enqueue_no += 1

    return task_list

# Generate 100 random task lists
random_task_lists = [generate_random_tasks() for _ in range(100)]

# Question 4
measure_time = lambda queue_class, task_lists: [
    timeit.timeit(lambda: [queue_class().enqueue(random.randint(1, 100)) if task == "enqueue" else queue_class().dequeue() for task in tasks], number=1)
    for tasks in task_lists
]

# Execution times
array_queue_times = measure_time(ArrayQueue, random_task_lists)
linked_list_queue_times = measure_time(LinkedListQueue, random_task_lists)

# Question 5
plt.figure(figsize=(10, 6))
plt.hist(array_queue_times, bins=30, alpha=0.5, label='Array Queue', color='red')
plt.hist(linked_list_queue_times, bins=30, alpha=0.5, label='Linked List Queue', color='yellow')
plt.title('Distribution of Execution Times for Queue Implementations')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

'''
Discuss Results: The array-based queue generally executes faster than the linked list queue. 
This is because to inserting in the beginning of a list is slower than adding a new node in a linked list. 
But removing from the end of the list is faster than searching for the second-last node in a linked list.
Overall, for these implementations, the array-queue appears to work more efficiently.
'''