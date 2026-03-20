def function_register(accumulated_tuple):
    print("PRODUCT REGISTRATION")
    product_counter = 1
    continue_ciclo = "yes"

    while continue_ciclo == "yes":
        print(f"-------- Product {product_counter} --------")
        try:
            id_product = int(input("Enter the product ID: "))

            if id_product <= 0:
                print("The ID must be positive.")
                continue

            product_name = input("Enter the product name: ")
            unit_price = float(input("Enter the price: "))

            product = {
                "ID": id_product,
                "nombre": product_name,
                "price": unit_price
            }

            accumulated_tuple = accumulated_tuple + (product,)

            product_counter += 1
            continue_ciclo = input("Register another? (yes/no): ").lower()

        except ValueError:
            print("Invalid data.")

    return accumulated_tuple