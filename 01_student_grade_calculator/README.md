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
