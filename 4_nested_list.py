# https://www.hackerrank.com/challenges/nested-list/problem

student = int(input())
lt = []

# Gather names and grades of students
for _ in range(student):
    name = input()
    grade = float(input())
    lt.append([name, grade])
    # print(f"{name} :: {grade}")

# Sort the list of students based on their grades
lt.sort(key=lambda x: x[1])

# Find the second lowest grade
mini = lt[0][1]
second = None
for name, val in lt:
    if val > mini:
        second = val
        break

# If there is a second lowest grade, print the names of the students with that grade
if second is not None:
    second_lowest_students = [name for name, val in lt if val == second]
    second_lowest_students.sort()
    for name in second_lowest_students:
        print(name)
else:
    print("No student with a second lowest grade.")
