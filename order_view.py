def view_orders(orders, customers, products):
    if not orders:
        print("No orders registered.\n")
        return

    print("\n====== ORDERS LIST ======\n")

    for order_id, order_data in orders.items():
        print(f"Order ID: {order_id}")

        customer_id = order_data["customer_id"]
        customer = customers.get(customer_id, {})

        print(f"Customer: {customer.get('customer', 'Unknown')}")

        print("Products:")
        for product_id, product in order_data["products"].items():
            print(f"- {product['nombre']} | Price: {product['price']} | Quantity: {product['quantity']} | Subtotal: {product['subtotal']}")

        print(f"Total: ${order_data['total']}")
        print("-" * 30)