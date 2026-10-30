"""
Creating Custom Classes
"""

class Account:

    # initialize function
    def __init__(self, name, balance):
        self.name = name

        if balance < 0:
            raise ValueError("Initial balance must be greater than or equal to 0.")
    
        self.balance = balance

    # create custom method for class/object
    def deposit(self, amount):
        self.balance += amount

    # official string representation of our object
    def __repr__(self):
        return "Account name: " + self.name + " Balance: " + str(self.balance)


# create some account objects

account1 = Account("Big Blue", 100.50)
account2 = Account("Thistle", 200.50)

print(account1)
print(account2)

account1.deposit(50.5)
print(account1)