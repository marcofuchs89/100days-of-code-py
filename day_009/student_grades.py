from typing import Dict
from pprint import pprint


student_scores: Dict[str, int] = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

# DONE-1: Create an empty dictionary called student_grades.

student_grades: Dict[str, str] = {}

# DONE-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    if student_scores[student] >= 91:
        student_grades[student] = "Outstanding"
    elif student_scores[student] >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


# 🚨 Don't change the code below 👇
pprint(student_grades)
