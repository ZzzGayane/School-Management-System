from src.models.student import Student
from src.models.teacher import Teacher
from src.models.course import Course
from src.services.school import School

school = School()

teacher = Teacher()

student1 = Student("Anna", 35)
student2 = Student("Mariam", 17)

math = Course("Math")

school.add_person(teacher)
school.add_person(student1)
school.add_person(student2)

student1.enroll(math)
student2.enroll(math)

# Teacher assigns grades
teacher.assign_grade(student1, math, 90)
teacher.assign_grade(student2, math, 85)

# Display all people
school.display_all()

# Show course info
print(math)

# Show grades
print(student1.grades)
