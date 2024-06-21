class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.capacity
    
    def dequeue(self):
        # Check if queue is empty before dequeue()
        if self.is_empty():
            print("Queue is empty")
            return
        return self.queue.pop(0)
    
    def enqueue(self, value):
        # Check if queue is full before enqueue()
        if self.is_full():
            print("Queue is full")
            return
        return self.queue.append(value)
    
    def front(self):
        return self.queue[0]