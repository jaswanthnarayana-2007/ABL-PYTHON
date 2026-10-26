# Shopping Bill Generator

## Problem statement
Create an itemized shopping bill by collecting item names, prices and quantities.

## Objectives
- Practise list creation, append, traversal and loops.
- Calculate line totals and the final bill.

## Assumptions
Prices must be non-negative and quantities must be positive integers. No tax or discount is applied.

## Algorithm
1. Read the number of items and validate it.
2. For each item, read name, price and quantity.
3. Validate price and quantity, then store them in parallel lists.
4. If all entries are valid, calculate each line amount.
5. Add each amount to the total.
6. Display the itemized bill and total.

## Pseudocode
```text
START
READ n
IF n <= 0: DISPLAY error
ELSE
    CREATE items, prices, quantities lists
    FOR each item
        READ name, price, quantity
        IF price < 0 OR quantity <= 0: mark invalid and stop
        APPEND values to lists
    IF all entries valid
        total = 0
        FOR each index
            amount = price[index] * quantity[index]
            total = total + amount
            DISPLAY item and amount
        DISPLAY total
END
```

## Test cases
| Items | Expected |
|---|---|
| Pen ₹10 × 3; Book ₹50 × 2 | Total ₹130 |
| Notebook ₹40 × 1 | Total ₹40 |
| Quantity 0 | Invalid price or quantity |

## Conclusion
This project demonstrates lists, loops, validation and repeated calculations.

## Detailed test cases

See [test_cases.md](test_cases.md) for normal, boundary, and invalid-input test cases with expected results.
