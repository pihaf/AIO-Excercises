from stack_class import MyStack

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