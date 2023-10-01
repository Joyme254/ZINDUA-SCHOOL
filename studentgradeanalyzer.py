# Lists and Tuples in Python Coding Challenge Title: Student Grade Analyzer
# Description:
# You have been tasked with creating a grade analyzer program for a coding bootcamp. The program should take a list of student names and their corresponding grades and perform various operations on the data.
# Requirements:
# The program should define a function called grade_analyzer that takes two parameters:
# student_grades: a list of tuples where each tuple contains a student's name (string) and their grade (float).
# operation: a string indicating the desired operation to perform. Valid operations are: "average", "highest", and "lowest".
# The grade_analyzer function should return the result of the requested operation on the student grades.
# If the operation parameter is "average", the function should calculate and return the average grade of all the students.
# If the operation parameter is "highest", the function should return the highest grade among all the students.
# If the operation parameter is "lowest", the function should return the lowest grade among all the students.
# If the operation parameter is not one of the valid operations mentioned above, the function should raise a ValueError with an appropriate error message.
# Example Usage:
# python

# student_grades = [("Alice", 89.5), ("Bob", 92.3), ("Charlie", 78.9), ("David", 85.6)] 
# operation = "average" 
# result = grade_analyzer(student_grades, operation) 
# print(result) # Output: 86.825 

# operation = "highest" 
# result = grade_analyzer(student_grades, operation) 
# print(result) # Output: 92.3 

# operation = "lowest" 
# result = grade_analyzer(student_grades, operation) 
# print(result) # Output: 78.9 

# operation = "median" 
# result = grade_analyzer(student_grades, operation) 
# # Raises ValueError with appropriate error message 
# Note:
# You can assume that the student_grades list will always have at least one element.
# You are not allowed to use any built-in functions or libraries for calculating averages, maximums, or minimums. Implement the logic yourself using lists and tuples.
# Make sure your code is properly structured
# Good Luck & Happy Coding!