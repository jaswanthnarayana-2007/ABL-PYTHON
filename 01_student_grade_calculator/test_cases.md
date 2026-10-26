# Test Cases — Student Marks and Grade Calculator

Run `python main.py` separately for each test from this folder.

## Valid and boundary inputs

| Test | Student | Marks for the five subjects | Expected result |
|---|---|---|---|
| 1 — Grade A | Ravi | 85, 90, 78, 88, 89 | Total 430/500, percentage 86%, PASS, Grade A |
| 2 — Fail due to one subject | Asha | 90, 90, 90, 90, 20 | Total 380/500, percentage 76%, FAIL, Grade F because one mark is below 35 |
| 3 — Grade B | Kiran | 95, 85, 75, 65, 55 | Total 375/500, percentage 75%, PASS, Grade B |
| 4 — Minimum passing mark | Mina | 35, 35, 35, 35, 35 | Total 175/500, percentage 35%, PASS, Grade D |
| 5 — Zero marks | Sam | 0, 0, 0, 0, 0 | Total 0/500, percentage 0%, FAIL, Grade F |
| 6 — Maximum marks | Diya | 100, 100, 100, 100, 100 | Total 500/500, percentage 100%, PASS, Grade A+ |
| 7 — Invalid mark above range | Arun | Enter 120 for any subject | Displays “Invalid marks. Marks must be between 0 and 100.” No result is calculated |
| 8 — Invalid mark below range | Neha | Enter -1 for any subject | Displays “Invalid marks. Marks must be between 0 and 100.” No result is calculated |
| 9 — Non-numeric input | Alex | Enter `hello` for a mark | Displays “Invalid input. Please enter a number.” No result is calculated |

## How to test

1. Open a terminal in the `01_student_grade_calculator` folder.
2. Run `python main.py`.
3. Enter the student name and five marks as described in the selected test.
4. Compare the program output with the expected result above.
5. Restart the program before running the next test.

## Notes

- The program expects exactly five numeric marks, each from 0 to 100.
- A mark below 35 means FAIL, even if the overall percentage is high.
- Grade thresholds are illustrative: A+ >= 90, A >= 80, B >= 70, C >= 60, otherwise D.
- Confirm the official grading rules with your faculty before final submission.
