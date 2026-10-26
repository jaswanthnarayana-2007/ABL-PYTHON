# Student Attendance Percentage Calculator

total_classes = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))

if total_classes <= 0:
    print("Total classes must be greater than zero")
elif attended < 0 or attended > total_classes:
    print("Invalid attendance details")
else:
    percentage = attended / total_classes * 100
    print("Attendance percentage:", round(percentage, 2), "%")

    # 75% is an example threshold; follow your college rules if different.
    if percentage >= 75:
        print("Status: Eligible")
    else:
        print("Status: Not eligible")
