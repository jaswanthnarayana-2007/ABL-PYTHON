# Test Cases — Student Marks Analysis

Marks must be between 0 and 100 inclusive.

| # | Number of subjects | Marks | Expected result |
|---|---:|---|---|
| 1 | 5 | 80, 90, 70, 60, 100 | Highest 100, lowest 60, total 400, average 80.0, passed 5 |
| 2 | 3 | 35, 34, 0 | Highest 35, lowest 0, total 69, average 23.0, passed 1 |
| 3 | 2 | 100, 100 | Highest 100, lowest 100, total 200, average 100.0, passed 2 |
| 4 | 3 | 0, 0, 0 | Highest 0, lowest 0, total 0, average 0.0, passed 0 |
| 5 | 0 | — | Number of subjects must be positive |
| 6 | 2 | 75, 120 | Invalid marks. Marks must be from 0 to 100. |
| 7 | 1 | -1 | Invalid marks. Marks must be from 0 to 100. |