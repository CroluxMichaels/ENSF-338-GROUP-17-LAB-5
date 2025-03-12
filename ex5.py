# Question 1

class CircularQueueArray:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = -1
        self.tail = -1

    def is_empty(self):
        return self.head == -1
    
    def is_full(self):
        return (self.tail + 1) % self.size == self.head
    
    def enqueue(self, element):
        if self.is_full():
            print("enqueue None")
            return
        if self.is_empty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = element
        print(f"enqueue {element}")
    
    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None
        element = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        print(f"dequeue {element}")
        return element
    
    def peek(self):
        if self.is_empty():
            print("peek None")
            return None
        print(f"peek {self.queue[self.head]}")
        return self.queue[self.head]

# Question 2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueueLinkedList:
    def __init__(self, capacity=5):  # Set capacity as 5 
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        if self.is_full():
            print("enqueue None")  # Queue is full
            return
        
        new_node = Node(element)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head 
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        
        self.size += 1
        print(f"enqueue {element}")


    def dequeue(self):
        if self.is_empty():
            print("dequeue None")  # Queue is empty
            return None
        
        element = self.head.data
        if self.head == self.tail:  
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head  
        
        self.size -= 1
        print(f"dequeue {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("peek None")  # Queue is empty
            return None
        print(f"peek {self.head.data}")
        return self.head.data

# Question 3

# Test List of 40 Operations
Mylist = CircularQueueLinkedList(5)  # For the linked list-based queue

Mylist.enqueue(1)  # Expected: "enqueue 1"
Mylist.enqueue(2)  # Expected: "enqueue 2"
Mylist.enqueue(3)  # Expected: "enqueue 3"
Mylist.peek()  # Expected: "peek 1"
Mylist.dequeue()  # Expected: "dequeue 1"
Mylist.dequeue()  # Expected: "dequeue 2"
Mylist.enqueue(4)  # Expected: "enqueue 4"
Mylist.enqueue(5)  # Expected: "enqueue 5"
Mylist.enqueue(6)  # Expected: "enqueue 6"
Mylist.peek()  # Expected: "peek 3"
Mylist.enqueue(7)  # Expected: "enqueue 7"
Mylist.enqueue(8)  # Expected: "enqueue None"
Mylist.dequeue()  # Expected: "dequeue 3"
Mylist.dequeue()  # Expected: "dequeue 4"
Mylist.dequeue()  # Expected: "dequeue 5"
Mylist.peek()  # Expected: "peek 6"
Mylist.dequeue()  # Expected: "dequeue 6"
Mylist.dequeue()  # Expected: "dequeue 7"
Mylist.peek()  # Expected: "peek None"
Mylist.dequeue()  # Expected: "dequeue None"
Mylist.enqueue(9)  # Expected: "enqueue 9"
Mylist.enqueue(10)  # Expected: "enqueue 10"
Mylist.enqueue(11)  # Expected: "enqueue 11"
Mylist.peek()  # Expected: "peek 9"
Mylist.enqueue(12)  # Expected: "enqueue 12"
Mylist.enqueue(13)  # Expected: "enqueue 13"
Mylist.enqueue(14)  # Expected: "enqueue None"
Mylist.dequeue()  # Expected: "dequeue 9"
Mylist.dequeue()  # Expected: "dequeue 10"
Mylist.dequeue()  # Expected: "dequeue 11"
Mylist.peek()  # Expected: "peek 12"
Mylist.enqueue(14)  # Expected: "enqueue 14"
Mylist.enqueue(15)  # Expected: "enqueue 15"
Mylist.dequeue()  # Expected: "dequeue 12"
Mylist.dequeue()  # Expected: "dequeue 13"
Mylist.dequeue()  # Expected: "dequeue 14"
Mylist.peek()  # Expected: "peek 15"
Mylist.dequeue()  # Expected: "dequeue 15"
Mylist.dequeue()  # Expected: "dequeue None"
Mylist.peek()  # Expected: "peek None"
Mylist.enqueue(16)  # Expected: "enqueue 16"
