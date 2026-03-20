def function_register(products_dict):
    """
    This function allows the user to register multiple products.
    Products are stored in a dictionary using the product ID as the key.
    """

    print("=== PRODUCT REGISTRATION ===")
    
    product_counter = 1
    continue_loop = "yes"

    # Loop to keep registering products
    while continue_loop == "yes":
        print(f"-------- Product {product_counter} --------")
        
        try:
            # Ask for product ID
            product_id = int(input("Enter the product ID: "))

            # Validate that ID is positive
            if product_id <= 0:
                print("The ID must be positive.")
                continue

            # Check if ID already exists
            if product_id in products_dict:
                print("This product ID already exists.")
                continue

            # Ask for product name
            product_name = input("Enter the product name: ")

            # Ask for product price
            unit_price = float(input("Enter the price: "))

            # Create product dictionary
            product = {
                "id": product_id,
                "name": product_name,
                "price": unit_price
            }

            # Store product in dictionary using ID as key
            products_dict[product_id] = product

            print("Product registered successfully!\n")

            product_counter += 1

            # Ask user if they want to continue
            continue_loop = input("Register another? (yes/no): ").lower()

        except ValueError:
            print("Invalid data. Please enter correct values.\n")

    return products_dict
