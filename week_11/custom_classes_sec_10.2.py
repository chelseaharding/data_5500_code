class Account:
    """Represents a bank account with a name and balance."""
    
    def __init__(self, name, balance):
        """Initialize the Account object with a name and starting balance."""
        self.name = name
        
        # Validate that the starting balance is valid
        if balance < 0:
            raise ValueError("Initial balance must be greater than or equal to 0.")
        
        self.balance = balance
        
    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        
    def __repr__(self):
        """Official string representation of the object."""
        return f"Account(name='{self.name}', balance={self.balance:.2f})"


# 1. Instantiating objects (creating individual account objects from the blueprint)
account1 = Account("Jane Green", 50.00)
account2 = Account("John Blue", 127.50)

# 2. Inspecting the objects
print("Initial Accounts:")
print(account1)
print(account2)

# 3. Accessing individual attributes
print(f"\n{account1.name}'s current balance: ${account1.balance:.2f}")

# 4. Calling methods on specific objects
account1.deposit(25.50)
print(f"After deposit, {account1.name}'s balance: ${account1.balance:.2f}")