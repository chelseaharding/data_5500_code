"""
Access to Attributes
"""

class Account:

    # initialize function
    def __init__(self, name, balance):
        self.name = name

        if balance < 0:
            raise ValueError("Initial balance must be greater than or equal to 0.")
    
        self._balance = balance

    # create custom method for class/object
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    # official string representation of our object
    def __repr__(self):
        return "Account name: " + self.name + " Balance: " + str(self._balance)


account1 = Account("Big Blue", 50)
print("inital account", account1)

account1._balance = -10000
print("account now:", account1)