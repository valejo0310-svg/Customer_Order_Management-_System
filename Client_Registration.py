clients = ()
def customer_registration (clients):
    n = int(input("how many clients do you want to register?: "))

    for i in range(n):
        print("customer", i+1)

        ID = int (input("Customer's ID: "))
        name = input("Customer's name: ")
        email = input("Customer's email: ")

        clients = ( ID, name, email)

        clients = clients + (clients,)  # agregamos a la tupla

        print("Customer added successfully", i+1)
        print("Customer's ID:", ID)
        print("Customer's name:", name)
        print("Customer's email:", email)

    return clients
