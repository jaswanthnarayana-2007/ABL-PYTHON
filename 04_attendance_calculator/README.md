# Student Attendance Calculator

## Problem statement
Calculate a student's attendance percentage and display eligibility based on a threshold.

## Objectives
- Practise integer input, arithmetic and relational operators.
- Validate attendance counts using conditional statements.

## Assumptions
The example eligibility threshold is 75%. Use the official college rule if it differs.

## Algorithm
1. Read total classes and attended classes.
2. Validate that total classes is positive.
3. Validate that attended classes is between zero and total classes.
4. Calculate percentage = attended / total × 100.
5. Compare the percentage with 75%.
6. Display percentage and status.

## Pseudocode
```text
START
READ total_classes, attended
IF total_classes <= 0: DISPLAY error
ELSE IF attended < 0 OR attended > total_classes: DISPLAY invalid details
ELSE
    percentage = attended / total_classes * 100
    DISPLAY percentage
    IF percentage >= 75: DISPLAY Eligible
    ELSE: DISPLAY Not eligible
END
```

## Test cases
| Total | Attended | Expected |
|---:|---:|---|
| 100 | 82 | 82%; Eligible |
| 100 | 60 | 60%; Not eligible |
| 0 | 0 | Error |
| 50 | 55 | Invalid attendance details |

## Conclusion
This program applies arithmetic, comparisons and validation to a practical student scenario.

## Detailed test cases

See [test_cases.md](test_cases.md) for normal, boundary, and invalid-input test cases with expected results.
