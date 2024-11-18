#!/usr/bin/env python3
# Author: psingh647

class Student:

    # Initialize a new student object with name and ID
    def __init__(self, name, number):
        self.name = name
        # Ensure student number is always treated as a string
        self.number = str(number)
        self.courses = {}  # Dictionary to store courses and grades

    # Display student details (name and number)
    def displayStudent(self):
        return f"Student Name: {self.name}\nStudent Number: {self.number}"

    # Add a course and its grade to the student's record
    def addGrade(self, course, grade):
        self.courses[course] = grade  # Update the courses dictionary

    # Calculate and return the GPA, handles no courses gracefully
    def displayGPA(self):
        if not self.courses:  # Check if there are no courses
            return f"GPA of student {self.name} is 0.0"
        # Sum up all grades and calculate the average
        total_grades = sum(self.courses.values())
        return f"GPA of student {self.name} is {total_grades / len(self.courses):.1f}"

    # List all courses the student has passed (grades > 0.0)
    def displayCourses(self):
        # Use list comprehension to filter passed courses
        return [course for course, grade in self.courses.items() if grade > 0.0]


if __name__ == '__main__':
    # Create a student object and add grades for testing
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create another student with integer ID to demonstrate flexibility
    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)  # Example of a failed course

    # Print details for student1
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Print details for student2
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
