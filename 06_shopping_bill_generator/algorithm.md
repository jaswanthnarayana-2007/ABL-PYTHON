# Algorithm: Shopping Bill Generator

1. Start.
2. Create empty lists for item names, prices, and quantities.
3. Read the number of items.
4. If the number of items is zero or negative, display "Enter at least one item".
5. Otherwise, repeat for each item:
   - Read the item name.
   - Read its price and quantity.
   - If price is negative or quantity is zero or negative, display an error and stop collecting items.
   - Otherwise, store the name, price, and quantity in their respective lists.
6. If all items are valid:
   - Set total amount to zero.
   - For each item, calculate amount = price × quantity.
   - Add the amount to the total.
   - Display the item name, quantity, and amount.
   - Display the final total.
7. Stop.
