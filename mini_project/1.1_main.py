# def login():
#     email = input("Please enter Gmail: ")

#     while "@" not in email:
#         print("Invalid email")
#         email = input("Please enter Gmail Again: ")  
          
#     password = input("Enter password: ")
#     if email == "admin@gmail.com" and password == "1234":
#         print("You are successful login.")
#         print("Welcome")
#         return 

#     while email != "admin@gmail.com" and password != "1234":
#         if email == "admin@gmail.com" and password != "1234":
#             print("Password is incorrect")
#             password = input("Enter password again: ")
#         elif email != "admin@gmail.com" and password == "1234":
#             print("Gmail is incorrect")
#             email = input("Enter gmail again: ")
#         else:
#             print("invalid email and password")
#             email = input("Enter gamil: ")
#             password = input("Enter password: ")
#         if email == "admin@gmail.com" and password == "1234":
#             print("You are successful login.")
#             print("Welcome")
        
# login()



# chatgpt code 
def login():
    email = input("Please enter Gmail: ")

    while "@" not in email:
        print("Invalid email")
        email = input("Please enter Gmail again: ")
    
    password = input("Enter password: ")

    if email == "admin@gmail.com" and password == "1234":
        print("You are successfully logged in.")
        print("Welcome")
        return
    
    while email != "admin@gmail.com" or password != "1234":
        if email == "admin@gmail.com" and password != "1234":
            print("Password is incorrect")
            password = input("Enter password again: ")
        elif email != "admin@gmail.com" and password == "1234":
            print("Gmail is incorrect")
            email = input("Please enter Gmail again: ")
        else:
            print("Gmail and Password are incorrect")
            email = input("Please enter Gmail again: ")
            password = input("Enter password again: ")
        
        if email == "admin@gmail.com" and password == "1234":
            print("You are successfully logged in.")
            print("Welcome")
            return

login()
