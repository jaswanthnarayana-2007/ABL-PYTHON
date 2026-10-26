# Library Late-Fee Calculator
# Sample rule: Rs. 2/day for first 5 days, then Rs. 5/day.

days = int(input("Enter number of days overdue: "))

if days < 0:
    print("Invalid number of days")
elif days == 0:
    print("No fine")
elif days <= 5:
    fine = days * 2
    print("Library fine: Rs.", fine)
else:
    fine = 5 * 2 + (days - 5) * 5
    print("Library fine: Rs.", fine)
