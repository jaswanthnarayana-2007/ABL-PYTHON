# Student Marks and Grade Calculator
# Syllabus: input/output, type conversion, lists, loops, operators and if-elif-else.

SUBJECT_COUNT = 5
PASS_MARK = 35

name = input("Enter student name: ").strip()
marks = []

for i in range(SUBJECT_COUNT):
    try:
        mark = float(input("Enter marks for subject " + str(i + 1) + " (0-100): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        break

    if mark < 0 or mark > 100:
        print("Invalid marks. Marks must be between 0 and 100.")
        break

    marks.append(mark)
else:
    total = sum(marks)
    percentage = total / SUBJECT_COUNT

    print("\n----- STUDENT RESULT -----")
    print("Student name:", name)
    print("Subject marks:", marks)
    print("Total marks:", round(total, 2), "/", SUBJECT_COUNT * 100)
    print("Percentage:", round(percentage, 2), "%")

    if min(marks) < PASS_MARK:
        print("Result: FAIL")
        print("Grade: F")
    else:
        print("Result: PASS")
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "D"
        print("Grade:", grade)

    print("--------------------------")
