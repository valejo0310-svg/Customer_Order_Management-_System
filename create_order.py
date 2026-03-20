def create_order(orders, customers, products):
    if not customers:
        print("No customers registered.\n")
        return orders

    if not products:
        print("No products registered.\n")
        return orders

    print("\n====== CREATE ORDER ======\n")

    order_id = len(orders) + 1

    customer_id = input("Enter customer ID: ")

    if customer_id not in customers:
        print("Customer not found.\n")
        return orders

    order_products = {}
    total = 0
    continue_ciclo = "yes"

    while continue_ciclo == "yes":
        try:
            product_id = int(input("Enter product ID: "))

            product_found = None

            for product in products:
                if product["ID"] == product_id:
                    product_found = product
                    break

            if product_found is None:
                print("Product not found.")
                continue

            quantity = int(input("Enter quantity: "))

            subtotal = product_found["price"] * quantity
            total += subtotal

            order_products.append({
                "nombre": product_found["nombre"],
                "price": product_found["price"],
                "quantity": quantity,
                "subtotal": subtotal
            })

            continue_ciclo = input("Add another product? (yes/no): ").lower()

        except ValueError:
            print("Invalid data.")

    orders[order_id] = {
        "customer_id": customer_id,
        "products": order_products,
        "total": total
    }

    print(f"Order {order_id} created successfully!\n")

    return orders
