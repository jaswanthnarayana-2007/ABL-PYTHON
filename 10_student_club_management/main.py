# Student Club Management using set operations

coding_club = set(input("Enter coding club roll numbers separated by spaces: ").split())
sports_club = set(input("Enter sports club roll numbers separated by spaces: ").split())

print("\nCoding club members:", coding_club)
print("Sports club members:", sports_club)
print("Members in either club (union):", coding_club | sports_club)
print("Members in both clubs (intersection):", coding_club & sports_club)
print("Only coding club members:", coding_club - sports_club)

roll = input("Enter a roll number to search: ")
if roll in coding_club or roll in sports_club:
    print("Student is a member of at least one club")
else:
    print("Student is not a member of either club")
