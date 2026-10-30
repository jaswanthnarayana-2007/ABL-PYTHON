# ATM Menu Simulation

## Problem statement
Build a simple console-based ATM menu that can show a balance, deposit money, withdraw money and exit.

## Objectives
- Practise while loops, if/elif/else, break and assignment operators.
- Maintain and update a balance variable.

## Assumptions
The starting balance is ₹5,000. This is a classroom simulation only and is not connected to any bank.

## Algorithm
1. Initialize balance to 5000.
2. Display the menu repeatedly.
3. Read the user's choice.
4. For balance, display the current balance.
5. For deposit, accept only a positive amount and add it to balance.
6. For withdrawal, accept only a positive amount not exceeding balance.
7. Exit on choice 4; otherwise report invalid choices.

## Pseudocode
```text
START
balance = 5000
WHILE true
    DISPLAY menu
    READ choice
    IF choice = 1: DISPLAY balance
    ELSE IF choice = 2: READ amount; if positive add to balance
    ELSE IF choice = 3: READ amount; validate and subtract if affordable
    ELSE IF choice = 4: DISPLAY thanks; BREAK
    ELSE: DISPLAY invalid choice
END WHILE
END
```

## Test cases
| Actions | Expected |
|---|---|
| Choose 1 | Shows ₹5,000 initially |
| Deposit ₹500, then choose 1 | Shows ₹5,500 |
| Withdraw ₹1,000 from ₹5,000 | Shows successful withdrawal |
| Withdraw ₹9,000 from ₹5,000 | Insufficient balance |
| Choose 4 | Program exits |

## Conclusion
This program applies repetition, branching, validation and updating a variable.

## Detailed test cases

See [test_cases.md](test_cases.md) for normal, boundary, and invalid-input test cases with expected results.

## Output previews

See the [screenshots folder](screenshots/README.md) for illustrative terminal-style output previews for three representative test cases. These are SVG previews, not captured terminal screenshots.


## Algorithm

See [algorithm.md](algorithm.md) for the step-by-step algorithm for this project.
