name = input("Enter student name: ")
mark1 = float(input("Enter marks for subject 1 (0-100): "))
mark2 = float(input("Enter marks for subject 2 (0-100): "))
mark3 = float(input("Enter marks for subject 3 (0-100): "))

total = mark1 + mark2 + mark3
percentage = (total / 300) * 100

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print(name)
print("Total:", f"{total}/300")
print("Percentage:", percentage, "%")
print("Grade:", grade)
