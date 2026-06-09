# Student Grade Management System
# A program to manage and analyze academic performance for a class.

# Inputs: List of student names and their respective grades (0-100).

# Logic: Store data using a list of dictionaries; calculate the class average, identify the highest/lowest grades, and filter students who fall below a passing threshold.

# Outputs: A structured summary including class average and a list of students needing academic support.

students_list = [
    {'student_name': 'Tony Stark', 'student_grade': 80},
    {'student_name': 'Peter Parker', 'student_grade': 95},
    {'student_name': 'Bruce Banner', 'student_grade': 72},
    {'student_name': 'Natasha Romanoff', 'student_grade': 88},
    {'student_name': 'Steve Rogers', 'student_grade': 91},
    {'student_name': 'Clint Barton', 'student_grade': 67},
    {'student_name': 'Thor Odinson', 'student_grade': 55},
    {'student_name': 'Wanda Maximoff', 'student_grade': 98},
    {'student_name': 'Vision', 'student_grade': 100},
    {'student_name': 'Scott Lang', 'student_grade': 63},
    {'student_name': 'Sam Wilson', 'student_grade': 77},
    {'student_name': 'Bucky Barnes', 'student_grade': 70},
    {'student_name': 'T\'Challa', 'student_grade': 93},
    {'student_name': 'Carol Danvers', 'student_grade': 85},
    {'student_name': 'Stephen Strange', 'student_grade': 96},
    {'student_name': 'James Rhodes', 'student_grade': 74},
    {'student_name': 'Nick Fury', 'student_grade': 82},
    {'student_name': 'Pepper Potts', 'student_grade': 89},
    {'student_name': 'Hope Van Dyne', 'student_grade': 78},
    {'student_name': 'Shuri', 'student_grade': 99},
]

def add_student():
    new_name = input('Type the new student name: ')
    new_grade = int(input(f'Type student {new_name} grade: '))
    new_list_item = {'student_name': new_name, 'student_grade': new_grade}
    students_list.append(new_list_item)

def class_average():
    grades_sum = 0
    for student in students_list:
        grades_sum += student['student_grade']
    avg_grade = int(grades_sum / len(students_list))
    print(f'The average grades are {avg_grade}.')

def get_grade(student): #Aux function - retrieves the grades given a dictionary
    return student['student_grade']

def top_students(students, top=3): # can change the top by changing here
    ranked = sorted(students, key=get_grade, reverse=True)[:top] # key precisa ser algo chamável — ou seja, algo que você consiga chamar com (). Se key=X é válido, então X(elemento) precisa funcionar
    print(f' -- Top {top} Best Grades in the class -- ')
    for student in ranked:
        print(f"Student: {student['student_name']} | Grade: {student['student_grade']}")



add_student()
class_average()
top_students(students_list, 5)

# for student in students_list:
#     print(f'Student: {student['student_name']} | Grade: {student['student_grade']}')