student_name = input("Enter the student's name: ")

grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))

average = (grade1 + grade2 + grade3) / 3

print("----Results----")
print("Student:", student_name)
print("Average:", round(average, 2))

if average >= 6:
    print("Status: Passed")
else:
    print("Status: Failed")