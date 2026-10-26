# Test Cases — Library Fine Calculator

Sample fine rule: Rs. 2/day for the first 5 overdue days, then Rs. 5/day for each additional day.

| # | Days overdue | Expected output |
|---|---:|---|
| 1 | 0 | No fine |
| 2 | 1 | Library fine: Rs. 2 |
| 3 | 5 | Library fine: Rs. 10 |
| 4 | 6 | Library fine: Rs. 15 |
| 5 | 10 | Library fine: Rs. 30 |
| 6 | -2 | Invalid number of days |

Note: fine rates are illustrative, not an official library policy.