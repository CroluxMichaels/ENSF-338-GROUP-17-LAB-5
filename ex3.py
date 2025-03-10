import random
import timeit
import matplotlib.pyplot as plt


# Q1 Implementation of stack that uses internal python .push() and .pop()
class ArrayStack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None


# Q2 Implementation of stack that uses singly-linked list .push() and .pop()
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        return None
    

# Q3 push and pop probability 
def generate_tasks(n=10000, push_prob=0.7):
    tasks = []
    for _ in range(n):
        if random.random() < push_prob:
            tasks.append(("push", random.randint(1, 100)))
        else:
            tasks.append(("pop", None))
    return tasks

def execute_tasks(stack, tasks):
    for operation, value in tasks:
        if operation == "push":
            stack.push(value)
        else:
            stack.pop()

# Q4 Performance of both implementations of stack .push() and .pop() - arrays and linkedlist
def measure_performance(stack_class, num_trials=100, num_tasks=10000):
    results = []
    for _ in range(num_trials):
        tasks = generate_tasks(num_tasks)
        stack = stack_class()
        execution_time = timeit.timeit(lambda: execute_tasks(stack, tasks), number=1)
        results.append(execution_time)
    return results

# Measure performance
array_stack_times = measure_performance(ArrayStack)
linked_list_stack_times = measure_performance(LinkedListStack)

print("Array stack time: ", array_stack_times)
print("Linkedlist stack time: ", linked_list_stack_times)


# Q5 Distributions for each implementation 
plt.plot(sorted(array_stack_times), label='Array Stack')
plt.plot(sorted(linked_list_stack_times), label='Linked List Stack')
plt.xlabel("Trial Number")
plt.ylabel("Execution Time (seconds)")
plt.title("Performance Comparison of Stack Implementations")
plt.legend()
plt.show()
