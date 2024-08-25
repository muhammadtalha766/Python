def show():
    print(f"Your current balance is Rs.{balance:.2f}")

def deposit():
    amount = float(input("Enter amount for deposit: "))
    
    if amount < 0:
        print("Amount must be in positive number.")
    else:
        amount += balance

def withdraw():
    pass

balance = 0
is_running = True

while is_running:
    print("--------------")
    print("Banking system")
    print("Press 1 for check your current balance.") 
    print("Press 2 for Deposit amount.") 
    print("Press 3 for withdraw.") 
    print("Press 4 for exit.\n") 
    
    choice = input("choice any option: ")
    if choice == "1":
        show()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid Number. Please enter a valid number (0-4)")