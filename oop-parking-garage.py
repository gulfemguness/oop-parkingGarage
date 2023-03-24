"""
Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). 

Your parking garage class should have the following methods:

1 takeTicket
- This should decrease the amount of tickets available by 1
    #remove
- This should decrease the amount of parkingSpaces available by 1
    #remove

3 payForParking
- Display an input that waits for an amount from the user and store it in a variable
- If the payment variable is not empty then (meaning the ticket has been paid) 
display a message to the user that their ticket has been paid and they have 15mins to leave
- This should update the "currentTicket" dictionary key "paid" to True

2 leaveGarage
- If the ticket has been paid, display a message of "Thank You, have a nice day"
- If the ticket has not been paid, display an input prompt for payment
- Once paid, display message "Thank you, have a nice day!"
- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
- Update tickets list to increase by 1 (meaning add to the tickets list)

You will need a few attributes as well:
- tickets -> list
- parkingSpaces -> list
- currentTicket -> dictionary

"""


class ParkingGarage():

    def __init__(self, count): 
        self.business_name = "One Price Parking"
        self.tickets = list(range(1, count + 1)) # list
        self.parkingSpaces = self.tickets[:] # [:] copies the list 
        self.currentTicket = {"paid": False} # dictionary

    def takeTicket(self):
    # This should decrease the amount of tickets available by 1
    # This should decrease the amount of parkingSpaces available by 1
        if not self.tickets:
            print("We are sorry, the garage is full.")
        else:
            self.currentTicket["ticket_number"] = self.tickets.pop()
            print(f"Please take your ticket.")


    def payForParking(self):
        # Display an input that waits for an amount from the user and store it in a variable
        # If the payment variable is not empty (meaning the ticket has been paid)
        # then display a message to the user that their ticket has been paid and they have 15mins to leave
        # this should update the "currentTicket" dictionary key "paid" to True
        user_input = int(input("Total Due is $10. Please enter the exact amount to pay:"))
        if user_input == 10:
            print("Thanks for your payment. You have 15 minutes to leave.")
            self.currentTicket["paid"] = True
        else:
            print("Input is invalid. Please enter the specified amount:")
            
    def leaveGarage(self):
        # If the ticket has been paid, display a message of "Thank You, have a nice day"
        # If the ticket has not been paid, display an input prompt for payment
        # Once paid, display message "Thank you, have a nice day!"
        # Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
        # Update tickets list to increase by 1 (meaning add to the tickets list)
        if self.currentTicket["paid"] == True:
            self.tickets.append(self.currentTicket["ticket_number"])
            print("Thank you! Have a nice day.")
        else:
            self.payForParking()

    def run(self):
        while True:
            response = input(f""" 
                                Welcome to {self.business_name}. Please select one of the options below:

                                Press 1 to Get Ticket
                                Press 2 to Leave
                        """)
            if response == '1':
                self.takeTicket()
            elif response == '2':
                self.leaveGarage()
            else:
                print("Your input is invalid. Please press 1 to Get Ticket or press 2 to Leave")
    

garage = ParkingGarage(50)
garage.run()





