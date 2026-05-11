from .person import Person

class Student(Person):

    def display_info(self):
        return "Student"

    def get_role(self):
        return "Student"
