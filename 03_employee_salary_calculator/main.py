# Employee Salary Calculator
# Assumptions: HRA = 20%, DA = 10%, PF deduction = 12% of basic salary.

name = input("Enter employee name: ")
basic = float(input("Enter basic salary: Rs. "))

if basic < 0:
    print("Invalid salary")
else:
    hra = basic * 0.20
    da = basic * 0.10
    pf = basic * 0.12
    gross = basic + hra + da
    net = gross - pf

    print("\nEmployee:", name)
    print("Basic salary: Rs.", round(basic, 2))
    print("HRA: Rs.", round(hra, 2))
    print("DA: Rs.", round(da, 2))
    print("PF deduction: Rs.", round(pf, 2))
    print("Gross salary: Rs.", round(gross, 2))
    print("Net salary: Rs.", round(net, 2))
