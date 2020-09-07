 

print("Welcome to Grade sorting app!")
print()

grade = [] 

grade.append(int(input("What is your first grade (0-100): ")))
grade.append(int(input("What is your second grade (0-100): ")))
grade.append(int(input("What is your thired grade (0-100): ")))
grade.append(int(input("What is your fourth grade (0-100): ")))

print(f"Your Grade are: {grade}")
print()
grade.sort(reverse=True)
print("Your grades from heighest to lowest: ",grade)

print("The lowest two grades will now be dropped.")
print("Removed grade: ",grade.pop())
print("Removed grade: ",grade.pop())

print("Your remining grades are: ", grade)
print(f"Nice Work!, Your heighest grade is {grade[0]}")