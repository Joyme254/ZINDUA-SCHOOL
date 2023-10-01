


# float('inf') represents positive infinity. It is a special floating-point value that represents a number greater than any other numerical value (positive or negative).
#  Similarly, float('-inf') represents negative infinity, a value less than any other numerical value.
#When you don't intend to use the value of a variable, you can use _ as a placeholder to indicate that the variable is intentionally ignored.



def calculate_average(student_grades):
    total = 0
    count = 0
    for _, grade in student_grades:
        total += grade
        count += 1
    if count == 0:
        return 0
    return total / count

def find_highest_grade(student_grades):
    highest_grade = float('-inf')
    for _, grade in student_grades:
        if grade > highest_grade:
            highest_grade = grade
    return highest_grade

def find_lowest_grade(student_grades):
    lowest_grade = float('inf')
    for _, grade in student_grades:
        if grade < lowest_grade:
            lowest_grade = grade
    return lowest_grade

def grade_analyzer(student_grades, operation):
    if operation == "average":
        return calculate_average(student_grades)
    elif operation == "highest":
        return find_highest_grade(student_grades)
    elif operation == "lowest":
        return find_lowest_grade(student_grades)
    else:
        print("Invalid operation. Valid operations are: 'average', 'highest', 'lowest'.")
    

student_grades = [('Mary', 78.50), ('John', 89.30), ('Peter', 40.70), ('Paul', 90.70)]

result = grade_analyzer (student_grades, 'average')
print (result)

result = grade_analyzer (student_grades, 'highest')
print (result)

result = grade_analyzer (student_grades, 'lowest')
print (result)