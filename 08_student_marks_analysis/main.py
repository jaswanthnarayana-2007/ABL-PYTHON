# Student Marks Analysis using a list

marks = []
n = int(input("Enter number of subjects: "))

if n <= 0:
    print("Number of subjects must be positive")
else:
    valid = True
    for i in range(n):
        mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
        if mark < 0 or mark > 100:
            print("Invalid marks. Marks must be from 0 to 100.")
            valid = False
            break
        marks.append(mark)

    if valid:
        passed = 0
        for mark in marks:
            if mark >= 35:
                passed += 1
        print("Marks:", marks)
        print("Highest:", max(marks))
        print("Lowest:", min(marks))
        print("Total:", sum(marks))
        print("Average:", round(sum(marks) / len(marks), 2))
        print("Subjects passed:", passed)
