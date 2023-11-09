class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id


class Teacher(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
