from First_registration import customer_registration #Importing the registration of the customer's function
#Creation of the main function
#Function used to call all the other functions on the main archive
def main ():
    print ("""
    ==========================================
      ~ welcome to the registration system ~ 
    ==========================================
    """.center(60)) #Welcome message to the system
    
    #Variable created to keep asking if there are going to be more customers added
    continuar = "yes" 
    #Loop created to keep asking
    while continuar in ["y","yes","Y","YES"]: 
        #Variables created to store all the client's data such as Id, names and emails
        ID_valido = False #Variable 
        while ID_valido == False:
          try:
              customer_ID = int (input ("Please enter customer's ID:"))
              if customer_ID < 0: 
                print("The ID can not be negative nor a 0.")
              else:
                  break  
          except ValueError:
                  print ("Please enter the right value.") 
               
        client_name = input ("\nPlease enter the customer's name: ")
        email = input ("\nPlease enter the customer´s email: ")
        #Creation of the variable "customer" to call the registration function
        customer = customer_registration(customer_ID, client_name, email) 
        #Print used to show the variable that contains the costumer's info
        print (customer)
        #Allows the system to ask if they want to keep adding customers
        continuar = input ("Do yo wish to keep adding new customers? (y/n): ")
        if continuar:
            print (customer_registration(customer_ID, client_name, email)) #Makes the system ask again
        

        



main ()#Calling the main function