# Student Marks and Grade Calculator

## Problem statement
Create a program that accepts a student's name and marks in five subjects, then calculates the total, percentage, pass/fail result, and grade.

## Objectives
- Practise input/output, type conversion, lists and arithmetic.
- Apply conditions to determine the result and grade.

## Assumptions
- There are five subjects, each scored from 0 to 100.
- A mark below 35 in any subject means the student fails.
- Grade thresholds are illustrative: A+ >= 90, A >= 80, B >= 70, C >= 60, otherwise D.

## Algorithm
1. Read the student's name.
2. Read five marks and validate each mark.
3. If a mark is outside 0–100, display an error.
4. Otherwise calculate total and percentage.
5. Check whether any subject mark is below 35.
6. If the student passes, determine the grade using the percentage.
7. Display the results.

## Pseudocode
```text
START
READ name
marks = empty list
REPEAT 5 times
    READ mark
    IF mark < 0 OR mark > 100
        DISPLAY invalid marks
        STOP input process
    ELSE
        ADD mark to marks
IF 5 valid marks entered
    total = SUM(marks)
    percentage = total / 5
    IF minimum(marks) < 35: DISPLAY Fail
    ELSE choose grade using percentage thresholds
    DISPLAY total, percentage and grade
END
```

## Test cases
| Input marks | Expected result |
|---|---|
| 85, 90, 78, 88, 89 | Total 430; 86%; Grade A |
| 90, 90, 90, 90, 20 | Result Fail |
| 120 for any subject | Invalid marks message |

## Conclusion
This program demonstrates lists, loops, arithmetic calculations and decision-making statements.


## How to run
Make sure Python 3 is installed, open a terminal in this folder, and run:

```bash
python main.py
```

## Sample run
```text
Enter student name: Ravi
Enter marks for subject 1 (0-100): 85
Enter marks for subject 2 (0-100): 90
Enter marks for subject 3 (0-100): 78
Enter marks for subject 4 (0-100): 88
Enter marks for subject 5 (0-100): 89

----- STUDENT RESULT -----
Student name: Ravi
Subject marks: [85.0, 90.0, 78.0, 88.0, 89.0]
Total marks: 430.0 / 500
Percentage: 86.0 %
Result: PASS
Grade: A
--------------------------
```

## Concepts demonstrated
- `input()` and `print()` for input/output
- `float()` for type conversion
- Lists and `append()` to store marks
- `for` loop and `else` on a loop
- Arithmetic operators, `sum()` and `min()`
- `if`, `elif`, `else`, comparisons and validation

## Student submission checklist
- [ ] Run the program with valid marks.
- [ ] Test a mark below 35 and verify the FAIL result.
- [ ] Test a mark outside 0–100 and verify validation.
- [ ] Capture your own terminal output screenshot.
- [ ] Confirm grading thresholds with your faculty before final submission.


## Algorithm

See [algorithm.md](algorithm.md) for the step-by-step algorithm for this project.
