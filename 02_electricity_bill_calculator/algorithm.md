# Algorithm: Electricity Bill Calculator

1. Start.
2. Read the number of electricity units consumed.
3. If units are negative, display "Invalid units".
4. Otherwise, calculate the bill using the progressive sample tariff:
   - If units are at most 100, bill = units × 1.50.
   - Else if units are at most 200, bill = (100 × 1.50) + ((units − 100) × 2.50).
   - Otherwise, bill = (100 × 1.50) + (100 × 2.50) + ((units − 200) × 4.00).
5. Display the bill rounded to two decimal places.
6. Stop.

**Note:** These are demonstration rates, not an official electricity tariff.
