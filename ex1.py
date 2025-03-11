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

def evaluate(stack):
    element = stack.pop()

    if element == '(':
        operator = stack.pop()
        items = []

        while stack.peek() != ')':
            items.append(evaluate(stack))

        stack.pop()

        if operator == '+':
            return sum(items)
        elif operator == '-':
            return items[0] - sum(items[1:])
        elif operator == '*':
            result = items[0]
            for i in items[1:]:
                result *= i
            return result
        elif operator == '/':
            result = items[0]
            for i in items[1:]:
                result /= i
            return result
    else:
        return float(element)
    

def main(expression):
    
    stack = MyArrayStack()
    list = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    list.reverse()
    for i in list:
        stack.push(i)

    result = evaluate(stack)
    print(result)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("No expression provided.")
        print("Please enter an appropriate expression as a command-line argument when running the program.")        