#!/usr/bin/python

# create a new list of students!
students = ["Jack", "Molly", "Maddie", "Kevin", "Bob", "Squirrel"];
student_id = 1

# print each student with their student #!
for student in students:
    print student_id 
    print student
    student_id += 1

# add a new student then print the list again!
students.append("Charles")
print students

# print just the first 5 students
print students[:4]
