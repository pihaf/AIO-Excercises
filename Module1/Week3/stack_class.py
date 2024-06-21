class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.capacity
    
    def pop(self):
        # Check if stack if empty before pop()
        if self.is_empty():
            print("Stack is empty")
            return
        return self.stack.pop()
    
    def push(self, value):
        # Check if stack is full before push()
        if self.is_full():
            print("Stack is full")
            return
        return self.stack.append(value)
        
    def top(self):
        # Check if stack if empty before top()
        if self.is_empty():
            print("Stack is empty")
            return
        return self.stack[-1]