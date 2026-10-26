# Test Cases — Electricity Bill Calculator

Tariff assumptions: first 100 units at Rs. 1.50/unit, next 100 at Rs. 2.50/unit, units above 200 at Rs. 4/unit.

| # | Input units | Expected output |
|---|---:|---|
| 1 | 0 | Electricity bill: Rs. 0.0 |
| 2 | 50 | Electricity bill: Rs. 75.0 |
| 3 | 100 | Electricity bill: Rs. 150.0 |
| 4 | 150 | Electricity bill: Rs. 275.0 |
| 5 | 200 | Electricity bill: Rs. 400.0 |
| 6 | 250 | Electricity bill: Rs. 600.0 |
| 7 | -5 | Invalid units |

## Sample calculation
For 250 units: (100 × 1.50) + (100 × 2.50) + (50 × 4.00) = Rs. 600.00.

Note: these are demonstration rates, not an official electricity tariff.