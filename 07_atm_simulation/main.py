# ATM Menu Simulation (educational; no real banking connection)

balance = 5000.0

while True:
    print("\n--- ATM MENU ---")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print("Available balance: Rs.", round(balance, 2))
    elif choice == "2":
        amount = float(input("Enter deposit amount: Rs. "))
        if amount > 0:
            balance += amount
            print("Deposit successful")
        else:
            print("Enter a positive amount")
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: Rs. "))
        if amount <= 0:
            print("Enter a positive amount")
        elif amount <= balance:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    elif choice == "4":
        print("Thank you")
        break
    else:
        print("Invalid choice")
