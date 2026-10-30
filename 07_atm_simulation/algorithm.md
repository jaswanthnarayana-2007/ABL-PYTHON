# Algorithm: ATM Menu Simulation

1. Start.
2. Set the starting account balance to Rs. 5000.
3. Repeat until the user chooses Exit:
   - Display the ATM menu: Check balance, Deposit, Withdraw, Exit.
   - Read the user's choice.
   - If choice is Check balance, display the current balance.
   - If choice is Deposit:
     - Read the deposit amount.
     - If amount is positive, add it to the balance and display success.
     - Otherwise, display an error.
   - If choice is Withdraw:
     - Read the withdrawal amount.
     - If amount is not positive, display an error.
     - Else if amount is not greater than the balance, subtract it and display success.
     - Otherwise, display insufficient balance.
   - If choice is Exit, display a thank-you message and stop the loop.
   - For any other choice, display "Invalid choice".
4. Stop.

**Note:** This is an educational simulation only. It is not connected to a real bank or account.
