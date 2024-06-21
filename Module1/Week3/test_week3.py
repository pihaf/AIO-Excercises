from stack_class import MyStack
from queue_class import MyQueue

def test_stack():
    stack1 = MyStack(capacity=5)
    stack1.push(1)
    stack1.push(2)

    assert stack1.is_full() == False
    assert stack1.top() == 2
    assert stack1.pop() == 2
    assert stack1.top() == 1
    assert stack1.pop() == 1
    assert stack1.is_empty() == True

def test_queue():
    queue1 = MyQueue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)

    assert queue1.is_full() == False
    assert queue1.front() == 1
    assert queue1.dequeue() == 1
    assert queue1.front() == 2
    assert queue1.dequeue() == 2
    assert queue1.is_empty() == True