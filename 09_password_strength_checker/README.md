# Password Strength Checker

## Problem statement
Check password length and the presence of uppercase letters, lowercase letters, digits and special characters.

## Objectives
Practise strings, string methods, loops, Boolean values and logical operators.

## Assumptions
This classroom rule labels a password Strong if it has at least eight characters and includes all four character categories. It is not a complete security assessment.

## Algorithm
1. Read password and initialize four Boolean flags.
2. Traverse each character and update the matching flag.
3. If length is at least eight and all flags are true, display Strong.
4. Else if length is at least six, display Moderate; otherwise display Weak.

## Pseudocode
```text
START
READ password
SET upper, lower, digit, special = false
FOR each character: update its category flag
IF length >= 8 AND all flags: DISPLAY Strong
ELSE IF length >= 6: DISPLAY Moderate
ELSE DISPLAY Weak
END
```

## Test cases
| Password | Expected |
|---|---|
| `Python@123` | Strong |
| `python1` | Moderate |
| `abc` | Weak |
| `ABCDEFGH1!` | Moderate because lowercase is absent |

## Conclusion
Demonstrates string traversal, string methods, Boolean variables and logical conditions.

## Detailed test cases

See [test_cases.md](test_cases.md) for normal, boundary, and invalid-input test cases with expected results.

## Output previews

See the [screenshots folder](screenshots/README.md) for illustrative terminal-style output previews for three representative test cases. These are SVG previews, not captured terminal screenshots.


## Algorithm

See [algorithm.md](algorithm.md) for the step-by-step algorithm for this project.
