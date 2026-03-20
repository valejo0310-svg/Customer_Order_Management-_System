#create a function to register a customer
def customer_registration():
#In this function, the user will be asked to enter the customer's ID, name, and email. 
#The function will return a dictionary with the customer's information.
    customer_ID = input("Enter ID: ")
    name = input("Enter name: ")
    email = input("Enter email: ")
#The function will return a dictionary with the customer's information.

    registration = {
        "ID": customer_ID,
        "customer": name,
        "email": email
    }
#return the registration dictionary
    return registration
