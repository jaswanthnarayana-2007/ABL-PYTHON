# Algorithm: Student Marks Analysis

1. Start.
2. Create an empty list to store marks.
3. Read the number of subjects.
4. If the number of subjects is zero or negative, display an error message.
5. Otherwise, repeat for each subject:
   - Read the mark.
   - If the mark is below 0 or above 100, display an error and stop collecting marks.
   - Otherwise, add the mark to the list.
6. If all marks are valid:
   - Set the passed-subject count to zero.
   - Check each mark; if it is at least 35, increase the passed count by one.
   - Calculate and display the highest mark, lowest mark, total, and average.
   - Display the number of subjects passed.
7. Stop.
