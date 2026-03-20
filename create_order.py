def create_order(orders, customers, products):
    """
    Handles the creation of a new sales order by linking customers, 
    products, and calculating totals using dictionaries and tuples.
    """
    # 1. PRE-VALIDATION: Check if necessary data exists before starting
    if not customers:
        print("No customers registered.\n")
        return orders

    if not products:
        print("No products registered.\n")
        return orders

    print("\n====== CREATE ORDER ======\n")

    # 2. IDENTIFICATION: Generate a unique ID for the order based on dictionary length
    order_id = len(orders) + 1
    customer_id = input("Enter customer ID: ")

    # 3. CUSTOMER LOOKUP: Check if the ID exists as a key in the customers dictionary
    if customer_id not in customers:
        print("Customer not found.\n")
        return orders

    # 4. TEMPORARY STORAGE: Use a dictionary to collect products during the loop.
    # This avoids using lists and ensures product IDs are unique within the order.
    temp_products_dict = {} 
    total = 0
    continue_ciclo = "yes"

    while continue_ciclo == "yes":
        try:
            product_id = int(input("Enter product ID: "))

            product_found = None

            # 5. TUPLE SEARCH: Iterate through the 'products' tuple to find the ID (index 0)
            for product in products:
                if product[0] == product_id:
                    product_found = product
                    break

            if product_found is None:
                print("Product not found.")
                continue

            quantity = int(input("Enter quantity: "))

            # 6. CALCULATIONS: Access product price at index [2] of the tuple
            subtotal = product_found[2] * quantity
            total += subtotal

            # 7. RECORD CREATION: Save product details as a tuple: (Name, Price, Qty, Subtotal)
            # Storing them in a dictionary allows easy updates if the same ID is entered twice.
            temp_products_dict[product_id] = (
                product_found[1], # Name
                product_found[2], # Price
                quantity,         
                subtotal          
            )

            continue_ciclo = input("Add another product? (yes/no): ").lower()

        except ValueError:
            print("Invalid data.")

    # 8. DATA SEALING: Convert the dictionary values into a final immutable tuple of tuples
    order_products_tuple = tuple(temp_products_dict.values())

    # 9. FINAL STORAGE: Save the complete order into the main orders dictionary
    orders[order_id] = {
        "customer_id": customer_id,
        "products": order_products_tuple, # Immutable record of items bought
        "total": total
    }

    print(f"Order {order_id} created successfully!\n")

    return orders
