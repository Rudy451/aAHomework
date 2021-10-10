class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, el):
        self.queue.append(el)

    def dequeue(self):
        value = self.queue[0]
        self.queue = self.queue[1:len(self.queue)]
        return value

    def peek(self):
        return self.queue[0]

# Create stack instance
my_queue = Queue()

# Push element to end of queue
my_queue.enqueue(1)

# Push another element to end of queue
my_queue.enqueue(2)

# Pull first element from queue
print(my_queue.dequeue())

# Push an element to end of queue
my_queue.enqueue(3)

# Read first element from queue
print(my_queue.peek())
