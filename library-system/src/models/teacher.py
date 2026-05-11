from .person import Person

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def assign_grade(self, student, course, grade):
        student.grades[course.name] = grade

    def display_info(self):
        return f"Teacher: {self.name}, Age: {self.age}"

    def get_role(self):
        return "Teacher"
