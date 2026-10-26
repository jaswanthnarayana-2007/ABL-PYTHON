# Executed Test Case Screenshots

These terminal-style screenshots document the outputs from running `main.py` with the nine inputs in [test_cases.md](../test_cases.md). The Python program was executed for each input case; all nine outcomes matched the expected behavior.

| Test | Screenshot | Outcome |
|---|---|---|
| 1 — Grade A | [01_grade_A.svg](./01_grade_A.svg) | PASS — expected output matched |
| 2 — Fail due to one subject | [02_fail_one_subject.svg](./02_fail_one_subject.svg) | PASS — expected output matched |
| 3 — Grade B | [03_grade_B.svg](./03_grade_B.svg) | PASS — expected output matched |
| 4 — Minimum passing marks | [04_minimum_pass.svg](./04_minimum_pass.svg) | PASS — expected output matched |
| 5 — Zero marks | [05_zero_marks.svg](./05_zero_marks.svg) | PASS — expected output matched |
| 6 — Maximum marks | [06_maximum_marks.svg](./06_maximum_marks.svg) | PASS — expected output matched |
| 7 — Invalid mark above 100 | [07_above_range.svg](./07_above_range.svg) | PASS — invalid input rejected |
| 8 — Invalid mark below 0 | [08_below_range.svg](./08_below_range.svg) | PASS — invalid input rejected |
| 9 — Non-numeric input | [09_non_numeric.svg](./09_non_numeric.svg) | PASS — non-numeric input rejected |

Run locally from this folder with `python main.py` to reproduce the tests.
