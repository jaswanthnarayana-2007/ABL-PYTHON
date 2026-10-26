# Test Cases — Attendance Calculator

Eligibility threshold used by this example: 75%.

| # | Total classes | Attended | Expected output |
|---|---:|---:|---|
| 1 | 100 | 90 | 90.0%; Eligible |
| 2 | 100 | 75 | 75.0%; Eligible |
| 3 | 100 | 74 | 74.0%; Not eligible |
| 4 | 40 | 30 | 75.0%; Eligible |
| 5 | 10 | 0 | 0.0%; Not eligible |
| 6 | 0 | 0 | Total classes must be greater than zero |
| 7 | 20 | 21 | Invalid attendance details |
| 8 | 20 | -1 | Invalid attendance details |

The 75% rule is an example only; use the official college attendance policy if different.