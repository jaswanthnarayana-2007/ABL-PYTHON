# Electricity Bill Calculator

## Problem statement
Calculate an electricity bill based on units consumed and a tiered demonstration tariff.

## Objectives
- Practise numeric input, arithmetic operators and an elif ladder.
- Apply different rates to different consumption ranges.

## Assumptions
For this exercise only: first 100 units cost ₹1.50/unit, units 101–200 cost ₹2.50/unit, and units above 200 cost ₹4/unit. These are sample rates, not an official tariff.

## Algorithm
1. Read units consumed.
2. If units are negative, show an error.
3. If units are at most 100, multiply all units by 1.50.
4. Else if units are at most 200, charge the first 100 at 1.50 and the remainder at 2.50.
5. Otherwise charge the first 100 at 1.50, the next 100 at 2.50, and the remainder at 4.00.
6. Display the bill.

## Pseudocode
```text
START
READ units
IF units < 0: DISPLAY invalid
ELSE IF units <= 100: bill = units * 1.50
ELSE IF units <= 200: bill = 150 + (units - 100) * 2.50
ELSE: bill = 150 + 250 + (units - 200) * 4
DISPLAY bill
END
```

## Test cases
| Units | Expected bill |
|---:|---:|
| 80 | ₹120 |
| 150 | ₹275 |
| 250 | ₹600 |
| -2 | Invalid units |

## Conclusion
This program demonstrates arithmetic calculations and multi-branch decision-making.

## Detailed test cases

See [test_cases.md](test_cases.md) for normal, boundary, and invalid-input test cases with expected results.

## Output previews

See the [screenshots folder](screenshots/README.md) for illustrative terminal-style output previews for three representative test cases. These are SVG previews, not captured terminal screenshots.


## Algorithm

See [algorithm.md](algorithm.md) for the step-by-step algorithm for this project.
