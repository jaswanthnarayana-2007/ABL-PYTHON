# Basic educational password strength checker
# This is a practice exercise, not a complete security assessment.

password = input("Enter a password: ")
has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Password strength: Strong")
elif len(password) >= 6:
    print("Password strength: Moderate")
else:
    print("Password strength: Weak")
