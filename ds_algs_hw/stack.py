class Stack:

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        value = self.stack[len(self.stack) - 1]
        self.stack = self.stack[0:len(self.stack)]
        return value

    def peek(self):
        return self.stack[len(self.stack) - 1]

# Create stack instance
my_stack = Stack()

# Push element to top of stack
my_stack.push(1)

# Push another element to top of stack
my_stack.push(2)

# Pull top element from stack
print(my_stack.pop())

# Push an element to top of stack
my_stack.push(3)

# Read element from top of stack
print(my_stack.peek())
