# Test Cases — Student Marks and Grade Calculator

Run `python main.py` separately for each test.

| Test | Student | Marks (5 subjects) | Expected result |
|---|---|---|---|
| 1 | Ravi | 85, 90, 78, 88, 89 | Total 430/500, 86%, PASS, Grade A |
| 2 | Asha | 90, 90, 90, 90, 20 | Total 380/500, 76%, FAIL, Grade F because one subject is below 35 |
| 3 | Kiran | 95, 85, 75, 65, 55 | Total 375/500, 75%, PASS, Grade B |
| 4 | Mina | 120 | Invalid marks message; no result calculated |
| 5 | Sam | Enter non-numeric text for a mark | Invalid input message; no result calculated |

## Notes
- The program expects five numeric marks between 0 and 100.
- A mark below 35 means FAIL, regardless of the overall percentage.
- Grade thresholds are examples for practice. Confirm the official grading rules with your faculty.
