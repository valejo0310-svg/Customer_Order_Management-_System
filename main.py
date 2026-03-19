#from First_registration import customer_registration #Importing the registration of the customer's function

print (f"""
╔═══════════════════════════════════════════════════════════╗
                🥑 RIWIMART RETAIL CHAIN 🥑
   🌷 Welcome to the Customer Order Management System! 🌷
╚═══════════════════════════════════════════════════════════╝""") #Some text formatting is used to make the welcome message more attractive
Menu = 1
while Menu:#Loop created to keep asking the user when they enter a wrong option
    try:          #Try and except created to catch the error when the user enters a non-integer value    
        Option = int(input(f"""{"-"*24} MAIN MENU {"-"*25} 
1) 🤵​  Enter Costumer 
2) 🍎  Enter Product 
3) ​🧾​  Create Order
4) ​🔍​  View Orders
5) 📋​  Generate Final Report
6) 💀​  Exit
{"="*60}
~ Please select an option:
➤  """)) # Some text formatting is used to make the menu more attractive  
        if Option < 1 or Option > 6: #Condition created to catch the error when the user enters a number that is not on the menu
            print(f"\n{'❌ ERROR: Please enter a valid number ❌':^60}\n") 
            Option = int(input(f"""{"-"*24} MAIN MENU {"-"*25} 
1) 🤵​  Enter Costumer 
2) 🍎  Enter Product 
3) ​🧾​  Create Order 
4) ​🔍  View Orders
5) 📋​  Generate Final Report
6) 💀​  Exit
{"="*60}
~ Please select an option:
➤  """))      
    except ValueError:
        print(f"\n{'❌ ERROR: Please enter a valid integer ❌':^60}\n")

#First condition created to call the function of the customer's registration when the user selects the first option of the menu.
#if Option == 1:

