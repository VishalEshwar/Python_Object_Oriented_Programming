class OnlineCourse:
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor
        self.students = []
        
    def enroll_students(self, name):
        self.students.append(name)
        print(f"{name} has been enrolled in the {self.course} course.")
        
    def course_details(self):
        print(f"Course: {self.course}")
        print(f"Instructor Name: {self.instructor}")  # Corrected the attribute name
        print(f"Enrolled Students: {', '.join(self.students)}")  # Corrected the attribute name
    
    def completed_course(self, name):
        if name in self.students:
            self.students.remove(name)
            print(f"{name} has completed the course.")
        else:
            print(f"{name} is not enrolled in the course.")
    
    def avg_grades(self, grades):
        total = sum(grades)
        average = total / len(grades) if grades else 0  # Handle division by zero
        print(f"The average grade is {average:.2f}")  # Formatted the average output

# Input for course and instructor
course_input = input("Enter a course: ").lower()
name = input("Enter an instructor: ").lower()
student = input("Enter a name: ").lower()

# Create an instance of OnlineCourse
course = OnlineCourse(course_input, name)

# Example grades
grades = [87, 98, 92, 93, 91]

# Call methods on the course instance
course.avg_grades(grades)
course.enroll_students(student)
course.course_details()
