from income_calculation import income_calculation

def final_report(orders, customers):
    if not orders:
        print("No data to generate report.\n")
        return

    print("\n====== FINAL REPORT ======\n")

    total_income = income_calculation(orders)
    print(f"Total income: ${total_income}")

    print(f"Total orders: {len(orders)}")
    print(f"Total customers: {len(customers)}")
