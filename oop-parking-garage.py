"""
Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). 


Your parking garage class should have the following methods:
- takeTicket
- This should decrease the amount of tickets available by 1
    #remove
- This should decrease the amount of parkingSpaces available by 1
    #remove

- payForParking
- Display an input that waits for an amount from the user and store it in a variable
- If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
- This should update the "currentTicket" dictionary key "paid" to True

-leaveGarage
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


# INSTANTIATE/making,building

# FUNCTION TO RUN METHODS on shoppingCart instance

# IDEA/BLUEPRINT

class Car():
    def __init__(self, plate, make):
        self.plate = plate
        self.make = make

    def __repr__(self):
        return f'{self.plate}, {self.make}'

class ParkingGarage():

    # ATTRIBUTES
    def __init__(self): 
        self.tickets = [] # list
        self.ticket_amount = 100
        self.parking_spaces = [] # list
        self.space_amount = 100
        self.current_ticket = {} # dictionary

    def takeTicket(self):
        self.ticket_amount.remove()
        self.parking_spaces.remove()

    def payForParking(self):
        userInput = input("")


# def run():
#     while True:
#         response = input(""" 
#                             Press 1 to Get Ticket
#                             Press 2 to Leave
#                     """)
#         if response == '1':
#             if 




