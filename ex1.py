import sys

# Stack Implementation taken from course GitHub

class MyArrayStack:
    def __init__(self):
        self._storage = []
    def push(self, value):
        self._storage.append(value)
    def pop(self):
        # Note that in Python "not <list>" evaluates to True if the list is empty
        if not self._storage:
            return None
        else:
            return self._storage.pop()
    def peek(self):
        if not self._storage:
            return None
        else:
            return self._storage[-1]
    def getlen(self):
        return len(self._storage)
    def reverse(self):
        self._storage.reverse()

def main(expression):
    print(f"Argument 1: {expression}")
    stack = MyArrayStack()
    for i in expression:
        stack.push(i)
    stack.reverse()
    while stack.getlen() > 0:
        print(stack.pop())

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("No expression provided.")        