#Importing functions from other files
from Client_Registration import customer_registration
from function_register import function_register
from income_calculation import income_calculation
from order_view import view_orders
from final_report import final_report
from create_order import create_order

#Initializing data structures that are gonna be used in the program
customers = {}
products = ()
orders = {}
#Welcome message
print(f"""
╔═══════════════════════════════════════════════════════════╗
                🥑 RIWIMART RETAIL CHAIN 🥑
   🌷 Welcome to the Customer Order Management System! 🌷
╚═══════════════════════════════════════════════════════════╝
""")
#Main menu loop
Menu = 1
#The main menu loop will continue until the user chooses to exit by selecting option 6.
# Inside the loop, the program will prompt the user to select an option 

while Menu:
    try:
        option = int(input(f"""{"-"*24} MAIN MENU {"-"*25}
1) 🤵 Enter Customer
2) 🍎 Enter Product
3) 🧾 Create Order
4) 🔍 View Orders
5) 📋 Generate Final Report
6) 💀 Exit
{"="*60}
➤ """))
# Depending on the user's choice, the program will execute the corresponding function:
        if option == 1:
            customer = customer_registration()
            customers[customer["ID"]] = customer
            print("Customer registered!\n")

        elif option == 2:
            products = function_register(products)

        elif option == 3:
            orders = create_order(orders, customers, products)

        elif option == 4:
            view_orders(orders, customers, products)

        elif option == 5:
            final_report(orders, customers)

        elif option == 6:
            print("Exiting...")
            Menu = 0

        else:
            print("Option not available.\n")

    except ValueError:
        print("❌ Invalid number.\n")
