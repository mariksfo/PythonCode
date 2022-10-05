# Expected Behaviour
# The user will enter the name of student
# The two details will be printed to console

# Details

# 1. Enter the name of student: Ben
# 2. Students age is: 10 
# 3. Is Student Tall ? : False


students = [
    {'name':'Alex', 'age': 12, 'isTall':True},
    {'name':'Ben', 'age': 10, 'isTall': False},
    {'name':'Ali','age': 15, 'isTall': True}
]

indexes = {'Alex':0, 'Ben':1, 'Ali':2}

name =  input('Enter the name of student: ')


# Steps to be taken

# Find the index of entered name in indexes
# Declare a variable student accessing the index of student in the list
# the variable student will be a dict now
# print above given details of student to the console

index = indexes[name]
print(index)

student = students[index]
print(student)

age = student['age']
tall = student['istall']

print("student's age is {} years".format(age))
print("is student tall? {}.format(tall)")