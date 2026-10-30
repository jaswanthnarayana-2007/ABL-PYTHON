# Algorithm: Basic Password Strength Checker

1. Start.
2. Read a password.
3. Set four flags to False: uppercase found, lowercase found, digit found, and special character found.
4. Examine each character in the password:
   - If it is uppercase, set the uppercase flag to True.
   - Else if it is lowercase, set the lowercase flag to True.
   - Else if it is a digit, set the digit flag to True.
   - Otherwise, set the special-character flag to True.
5. If the password has at least 8 characters and all four flags are True, display "Strong".
6. Else if the password has at least 6 characters, display "Moderate".
7. Otherwise, display "Weak".
8. Stop.

**Note:** This is a basic programming exercise, not a complete password-security assessment.
