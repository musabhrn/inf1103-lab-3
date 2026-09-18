inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity (or 'quit' to exit): ").strip()

    if user_input.lower() == "quit":
        break

    if not user_input.isdigit():
        print("Error. Invalid input. Please enter a non-negative number.")
        failed_entries += 1
        continue

    stock_quantity = int(user_input)

    inventory += stock_quantity

    if inventory > 500:
        print("Alert! Inventory total exceeds 500 units.")
        break


print("-------------------------------")
print(f"Total Units Processed: {inventory}")    
print(f"Number of Failed/Rejected Entries: {failed_entries}")