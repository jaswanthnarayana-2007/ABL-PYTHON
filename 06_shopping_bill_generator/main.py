# Shopping Bill Generator using lists and a for loop

items = []
prices = []
quantities = []

n = int(input("Enter number of items: "))

if n <= 0:
    print("Enter at least one item")
else:
    valid = True
    for i in range(n):
        name = input("Enter item name: ")
        price = float(input("Enter price: Rs. "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity <= 0:
            print("Invalid price or quantity")
            valid = False
            break

        items.append(name)
        prices.append(price)
        quantities.append(quantity)

    if valid:
        total = 0
        print("\n--- SHOPPING BILL ---")
        for i in range(n):
            amount = prices[i] * quantities[i]
            total += amount
            print(items[i], "x", quantities[i], "=", round(amount, 2))
        print("---------------------")
        print("Total amount: Rs.", round(total, 2))
