"""
Sentinel Values
"""

selection = 0

while selection != 5:
    print("Welcome to the happy message program!")
    print("Enter one of the following selections:")
    print("1. Show the weather")
    print("2. How is my day going to go?")
    print("Select 5 to quit")

    selection = int(input("Enter your selection: "))
    
    if selection == 1:
        print("The weather is great!")
    elif selection == 2:
        print("Your day will be amazing!")
    elif selection == 5:
        print("Thanks for using the happy message program!")