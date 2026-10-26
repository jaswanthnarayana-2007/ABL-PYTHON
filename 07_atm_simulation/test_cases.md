# Test Cases — ATM Simulation

Starting balance for every fresh run: Rs. 5000.00. This is a classroom simulation only; it does not connect to a bank.

| # | Menu/input sequence | Expected result |
|---|---|---|
| 1 | Choose 1 | Available balance: Rs. 5000.0 |
| 2 | Choose 2, deposit 1000, then choose 1 | Deposit successful; balance Rs. 6000.0 |
| 3 | Choose 3, withdraw 500, then choose 1 | Withdrawal successful; balance Rs. 4500.0 |
| 4 | Choose 3, withdraw 6000 | Insufficient balance |
| 5 | Choose 2, deposit 0 | Enter a positive amount |
| 6 | Choose 3, withdraw -10 | Enter a positive amount |
| 7 | Choose 9 | Invalid choice |
| 8 | Choose 4 | Thank you; program exits |

Amounts are entered as numbers. The simulation does not store balance between runs.