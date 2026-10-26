# Student Marks Analysis

## Problem statement
Accept marks for multiple subjects and report highest, lowest, total, average and subjects passed.

## Objectives
Practise lists, traversal, loops and built-in functions.

## Assumptions
Each mark is between 0 and 100. A mark of 35 or more counts as a pass for this example.

## Algorithm
1. Read a positive subject count.
2. Read and validate each mark, storing it in a list.
3. If all marks are valid, calculate maximum, minimum, total and average.
4. Count marks greater than or equal to 35.
5. Display the statistics.

## Pseudocode
```text
START
READ n
IF n <= 0: DISPLAY error
ELSE READ n marks and validate each
IF all marks valid
  total = SUM(marks); average = total / n
  count marks >= 35
  DISPLAY max, min, total, average and pass count
END
```

## Test cases
| Marks | Expected |
|---|---|
| 85, 72, 90, 68 | Highest 90; lowest 68; total 315; average 78.75; 4 passed |
| 30, 40, 35 | 2 subjects passed |
| 120 | Invalid marks |

## Conclusion
Demonstrates list traversal, built-in functions, conditions and numeric analysis.