def create_order(orders, customers, products):
    # Check if there are registered customers, if not, notify and return orders unchanged
    if not customers:
        print("No customers registered.\n")
        return orders

    # Check if there are registered products, if not, notify and return orders unchanged
    if not products:
        print("No products registered.\n")
        return orders

    print("\n====== CREATE ORDER ======\n")

    # Generate a new unique order ID based on the current number of orders
    order_id = len(orders) + 1

    # Ask the user to enter the customer ID for this order
    customer_id = input("Enter customer ID: ")

    # Validate that the entered customer ID exists in the customers dictionary
    if customer_id not in customers:
        print("Customer not found.\n")
        return orders

    # Dictionary to store the products added to this order, keyed by product ID
    order_products = {}

    # Accumulator for the total cost of the order
    total = 0

    # Control variable to keep the product-adding loop running
    continue_ciclo = "yes"

    # Loop to keep adding products until the user decides to stop
    while continue_ciclo == "yes":
        try:
            # Ask the user to enter the ID of the product they want to add
            product_id = int(input("Enter product ID: "))

            # Variable to store the matching product, starts as None
            product_found = None

            # Search through all products to find the one matching the entered ID
            for product in products:
                if product["ID"] == product_id:
                    product_found = product
                    break  # Stop searching once the product is found

            # If no product matched the entered ID, notify the user and restart the loop
            if product_found is None:
                print("Product not found.")
                continue

            # Ask the user how many units of the product they want to order
            quantity = int(input("Enter quantity: "))

            # Calculate the subtotal for this product (price × quantity)
            subtotal = product_found["price"] * quantity

            # Add the subtotal to the running total of the order
            total += subtotal

            # Store the product details in the order_products dictionary using product_id as key
            # If the same product_id is entered again, it will overwrite the previous entry
            order_products[product_id] = {
                "nombre": product_found["nombre"],     
                "price": product_found["price"],        
                "quantity": quantity,                  
                "subtotal": subtotal                   
            }

            # Ask the user if they want to add another product to the order
            continue_ciclo = input("Add another product? (yes/no): ").lower()

        except ValueError:
            # Handle the case where the user enters a non-numeric value for ID or quantity
            print("Invalid data.")

    # Save the completed order in the orders dictionary using the generated order ID as key
    orders[order_id] = {
        "customer_id": customer_id,    
        "products": order_products,     
        "total": total                  
    }

    print(f"Order {order_id} created successfully!\n")

    # Return the updated orders dictionary with the new order included
    return orders
