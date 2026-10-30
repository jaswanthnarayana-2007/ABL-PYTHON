# Algorithm: Student Marks and Grade Calculator

1. Start.
2. Read the student's name.
3. Create an empty list to store marks.
4. Repeat for five subjects:
   - Read the subject mark.
   - Convert it to a number.
   - If the input is not numeric, display an error and stop reading marks.
   - If the mark is below 0 or above 100, display an error and stop reading marks.
   - Otherwise, add the mark to the list.
5. If all five marks were entered:
   - Calculate the total of the marks.
   - Calculate percentage = total / 5.
   - Display the student's name, marks, total, and percentage.
   - If any mark is below 35, display FAIL and grade F.
   - Otherwise, display PASS and assign a grade:
     - 90 or above: A+
     - 80 to below 90: A
     - 70 to below 80: B
     - 60 to below 70: C
     - Below 60: D
6. Stop.

**Note:** The pass mark and grade boundaries are example rules and should be changed if your lecturer specifies different rules.
