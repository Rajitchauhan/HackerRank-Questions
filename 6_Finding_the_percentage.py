# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())

    student = {}
    for _ in range(n):
        key, *line = input().split()
        marks = list(map(float, line))
        student[key] = marks

    s_name = input()

    # Check if the student name exists in the dictionary
    if s_name in student:
        marks = student[s_name]
        average = sum(marks) / len(marks)
        print("{:.2f}".format(average))
    else:
        print("Student not found.")
