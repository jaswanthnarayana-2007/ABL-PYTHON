# Student Club Management Using Sets

## Problem statement
Represent two student clubs using sets and report their union, intersection, coding-only members and membership of a searched roll number.

## Objectives
Practise set creation, union, intersection, difference and membership testing.

## Assumptions
Roll numbers are space-separated strings. Sets automatically remove duplicate entries.

## Algorithm
1. Read roll numbers for both clubs and convert them to sets.
2. Display the sets, union, intersection and difference.
3. Read a roll number and test membership in either set.
4. Display the result.

## Pseudocode
```text
START
READ coding club and sports club values
coding = SET(values); sports = SET(values)
DISPLAY coding UNION sports
DISPLAY coding INTERSECTION sports
DISPLAY coding DIFFERENCE sports
READ roll
IF roll IN coding OR roll IN sports: DISPLAY member
ELSE DISPLAY not a member
END
```

## Test cases
| Coding club | Sports club | Expected |
|---|---|---|
| 101 102 103 | 102 103 104 | Union 101,102,103,104; intersection 102,103 |
| 101 105 | 105 106 | Coding-only member 101 |
| Search 106 in first example | — | Member of at least one club |

## Conclusion
Demonstrates set operations and membership testing. Set display order may vary.

## Detailed test cases

See [test_cases.md](test_cases.md) for normal, boundary, and invalid-input test cases with expected results.

## Output previews

See the [screenshots folder](screenshots/README.md) for illustrative terminal-style output previews for three representative test cases. These are SVG previews, not captured terminal screenshots.
