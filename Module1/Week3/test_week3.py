from stack_class import MyStack
from queue_class import MyQueue
from ward_person_oop import (Person, Student, Teacher, Doctor, Ward)

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

def test_ward_person_oop():
    student1 = Student(name ="studentA", yob=2010, grade ="7")
    student1.describe()

    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher1.describe()

    doctor1 = Doctor(name ="doctorA", yob=1945, specialist="Endocrinologists")
    doctor1.describe()

    teacher2 = Teacher(name ="teacherB", yob =1995, subject ="History")
    doctor2 = Doctor(name ="doctorB", yob =1975, specialist ="Cardiologists")
    ward1 = Ward(name ="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    assert ward1.count_doctor() == 2

    ward1.sort_age()
    assert ward1.compute_average() == 1982
