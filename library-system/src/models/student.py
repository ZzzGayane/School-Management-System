from .person import Person

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses = []
        self.grades = {}

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)

    def display_info(self):
        return f"Student: {self.name}, Age: {self.age}"

    def get_role(self):
        return "Student"
