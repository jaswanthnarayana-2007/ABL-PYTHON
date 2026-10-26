# Library Fine Calculator

## Problem statement
Calculate a library fine from the number of days a book is overdue.

## Objectives
- Practise input conversion, arithmetic and an elif ladder.
- Implement a simple rule-based fee calculation.

## Assumptions
The sample rule is ₹2 per day for the first five overdue days and ₹5 for each additional day. Replace it with your library's official rule if required.

## Algorithm
1. Read overdue days.
2. Reject negative input.
3. If days are zero, display no fine.
4. If days are 1–5, multiply days by 2.
5. Otherwise calculate ₹10 plus ₹5 for each day beyond five.
6. Display the fine.

## Pseudocode
```text
START
READ days
IF days < 0: DISPLAY invalid
ELSE IF days = 0: DISPLAY no fine
ELSE IF days <= 5: fine = days * 2
ELSE: fine = 10 + (days - 5) * 5
DISPLAY fine if calculated
END
```

## Test cases
| Overdue days | Expected result |
|---:|---|
| 0 | No fine |
| 3 | ₹6 |
| 5 | ₹10 |
| 8 | ₹25 |
| -1 | Invalid number of days |

## Conclusion
This program demonstrates conditions and arithmetic using a practical library example.

## Detailed test cases

See [test_cases.md](test_cases.md) for normal, boundary, and invalid-input test cases with expected results.

## Output previews

See the [screenshots folder](screenshots/README.md) for illustrative terminal-style output previews for three representative test cases. These are SVG previews, not captured terminal screenshots.
