from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name:str, yob:int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name: str, yob: int, grade:str):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(f'Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}')
    
class Teacher(Person):
    def __init__(self, name: str, yob: int, subject:str):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(f'Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}')
    
class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist:str):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(f'Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}')
    
class Ward:
    def __init__(self, name:str):
        self.__name = name
        self.__list_people = []

    def add_person(self, person:Person):
        self.__list_people.append(person)

    def describe(self):
        print(f'Ward name: {self.__name}')
        for person in self.__list_people:
            person.describe()

    def count_doctor(self):
        result = 0
        for person in self.__list_people:
            if isinstance(person, Doctor):
                result = result + 1
        return result
    
    def sort_age(self):
        self.__list_people.sort(key=lambda x: x.get_yob(), reverse=True)

    def compute_average(self):
        average = 0
        count = 0
        for person in self.__list_people:
            if isinstance(person, Teacher):
                average = average + person.get_yob()
                count = count + 1
        return average/count
    