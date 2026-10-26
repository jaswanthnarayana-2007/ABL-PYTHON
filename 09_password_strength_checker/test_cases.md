# Test Cases — Password Strength Checker

This is a beginner string-practice exercise, not a complete security audit.

| # | Password | Expected output | Reason |
|---|---|---|---|
| 1 | `Abcd123!` | Strong | At least 8 characters, uppercase, lowercase, digit, and special character |
| 2 | `abc123` | Moderate | Length is 6 or more, but not all strong conditions are met |
| 3 | `abc` | Weak | Fewer than 6 characters |
| 4 | `ABCDEFGH` | Moderate | Long enough but missing lowercase, digit, and special character |
| 5 | `Abcdef12` | Moderate | Length and letter/digit conditions pass, but no special character |
| 6 | `A1!bc` | Weak | Fewer than 6 characters |
| 7 | empty input | Weak | Length is below 6 |

Do not use real passwords when demonstrating or taking screenshots of this project.