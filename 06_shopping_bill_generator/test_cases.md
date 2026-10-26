# Test Cases — Shopping Bill Generator

| # | Input items | Expected output |
|---|---|---|
| 1 | 2 items: Pen, price 10, qty 3; Book, price 50, qty 2 | Pen x 3 = 30; Book x 2 = 100; total Rs. 130.0 |
| 2 | 1 item: Milk, price 32.5, qty 1 | Milk x 1 = 32.5; total Rs. 32.5 |
| 3 | Number of items = 0 | Enter at least one item |
| 4 | 1 item: Rice, price 60, qty 0 | Invalid price or quantity |
| 5 | 1 item: Soap, price -5, qty 2 | Invalid price or quantity |
| 6 | 1 item: Pencil, price 0, qty 4 | Valid; total Rs. 0.0 |

The program expects numeric input for count, price, and quantity. These test cases cover valid entries and basic validation.