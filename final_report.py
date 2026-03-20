from income_calculation import income_calculation

def final_report(orders, customers):
    """
    Generates a comprehensive summary of all transactions, 
    calculating totals and listing detailed order information.
    """
    # Check if the orders dictionary is empty to avoid processing empty data
    if not orders:
        print("No data to generate report.\n")
        return

    print("\n====== FINAL REPORT ======\n")

    # Call the utility function to sum all "total" fields from the orders dictionary
    total_income = income_calculation(orders)

    # Display general statistics using built-in len() for dictionaries
    print("Total income:", total_income)
    print("Total orders:", len(orders))
    print("Total customers:", len(customers))

    print("\n--- Orders detail ---")

    # Iterate through the orders dictionary (Key: order_id, Value: order_data_dict)
    for order_id, order in orders.items():
        print("Order ID:", order_id)

        # Retrieve the customer tuple using the ID stored in the order.
        # Uses .get() with a default tuple fallback to prevent KeyError.
        customer = customers.get(order["customer_id"], ("", "Unknown", ""))
        
        # Access index [1] because the customer name is the second element in the tuple
        print("Customer:", customer[1])

        print("Products:")
        # Loop through the tuple of product tuples stored within the order
        for product in order["products"]:
            # Product tuple structure: (Name [0], Price [1], Quantity [2], Subtotal [3])
            print("-", product[0], "| Qty:", product[2], "| Subtotal:", product[3])

        # Print the final total calculated during the order creation
        print("Total:", order["total"])
        print("-" * 30)
