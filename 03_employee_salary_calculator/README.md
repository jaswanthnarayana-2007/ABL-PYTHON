# Employee Salary Calculator

## Problem statement
Calculate an employee's allowances, gross salary, deduction and net salary from basic salary.

## Objectives
- Practise variables, numeric input and arithmetic operators.
- Organize calculations using meaningful variable names.

## Assumptions
HRA is 20% of basic salary, DA is 10%, and PF is 12% of basic salary. These percentages are for the assignment example only.

## Algorithm
1. Read employee name and basic salary.
2. Reject a negative basic salary.
3. Calculate HRA, DA and PF.
4. Calculate gross salary as basic + HRA + DA.
5. Calculate net salary as gross - PF.
6. Display the salary details.

## Pseudocode
```text
START
READ name, basic
IF basic < 0: DISPLAY invalid salary
ELSE
    hra = basic * 0.20
    da = basic * 0.10
    pf = basic * 0.12
    gross = basic + hra + da
    net = gross - pf
    DISPLAY salary details
END
```

## Test cases
| Basic salary | Expected gross | Expected net |
|---:|---:|---:|
| ₹20,000 | ₹26,000 | ₹23,600 |
| ₹10,000 | ₹13,000 | ₹11,800 |
| -100 | Invalid salary | Not calculated |

## Conclusion
This program demonstrates variables, arithmetic expressions, input validation and output formatting.

## Detailed test cases

See [test_cases.md](test_cases.md) for normal, boundary, and invalid-input test cases with expected results.

## Output previews

See the [screenshots folder](screenshots/README.md) for illustrative terminal-style output previews for three representative test cases. These are SVG previews, not captured terminal screenshots.


## Algorithm

See [algorithm.md](algorithm.md) for the step-by-step algorithm for this project.
