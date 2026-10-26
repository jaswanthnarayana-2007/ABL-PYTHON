# Student Marks and Grade Calculator
# Concepts: input/output, lists, arithmetic, conditions

name = input("Enter student name: ")
marks = []

for i in range(5):
    mark = float(input("Enter marks for subject " + str(i + 1) + " (0-100): "))
    if mark < 0 or mark > 100:
        print("Invalid marks. Enter a value from 0 to 100.")
        break
    marks.append(mark)
else:
    total = sum(marks)
    percentage = total / len(marks)

    print("\nStudent:", name)
    print("Marks:", marks)
    print("Total:", total, "/ 500")
    print("Percentage:", round(percentage, 2), "%")

    if min(marks) < 35:
        print("Result: Fail")
    elif percentage >= 90:
        print("Grade: A+")
    elif percentage >= 80:
        print("Grade: A")
    elif percentage >= 70:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    else:
        print("Grade: D")
