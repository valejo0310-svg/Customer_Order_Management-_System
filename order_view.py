def view_orders(orders, customers, products):
    """
    Iterates through the registered orders and displays them in a 
    readable format, pulling linked data from customers and products.
    """
    # 1. EMPTY STATE CHECK: Prevent the function from running if there's nothing to show
    if not orders:
        print("No orders registered.\n")
        return

    print("\n====== ORDERS LIST ======\n")

    # 2. DICTIONARY UNPACKING: 
    # 'order_id' is the key (ID), 'order_data' is the value (a dictionary of details)
    for order_id, order_data in orders.items():
        print("Order ID:", order_id)

        # 3. LINKING DATA: Extract the customer ID stored in the order
        customer_id = order_data["customer_id"]

        # 4. DEFENSIVE LOOKUP: 
        # Search for the customer in the 'customers' dictionary.
        # If not found, return a default tuple to prevent the program from crashing.
        customer = customers.get(customer_id, ("", "Unknown", ""))

        # 5. TUPLE ACCESS: 
        # Index [1] refers to the 'Name' in the customer tuple (ID, Name, Email)
        print("Customer:", customer[1]) 

        print("Products:")
        # 6. NESTED ITERATION: 
        # 'order_data["products"]' is a tuple containing other tuples (the items bought)
        for product in order_data["products"]:
            # 7. PRODUCT TUPLE MAPPING:
            # Based on create_order.py, the indices are:
            # product[0] -> Name
            # product[1] -> Price
            # product[2] -> Quantity
            print("-", product[0], "| Price:", product[1], "| Qty:", product[2])

        # 8. SUMMARY: Display the pre-calculated total from the order dictionary
        print("Total:", order_data["total"])
        print("-" * 30)
