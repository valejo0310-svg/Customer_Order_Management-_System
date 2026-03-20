def income_calculation(orders):
    """
    Calculates the cumulative income from all orders processed in the system.
    This function acts as the mathematical engine for the final reports.
    """
    # Initialize a counter to store the total accumulated money
    total_income = 0

    # Iterate through the values of the 'orders' dictionary.
    # Each 'order' represents an individual transaction dictionary.
    for order in orders.values():
        
        # Access the "total" key from each order and add it to our counter.
        # This value was pre-calculated and stored during the order creation.
        total_income += order["total"]

    # Return the final sum to the calling function (e.g., final_report)
    return total_income