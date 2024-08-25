# Q: check email and password is valid or invalid 
# email = "admin@gmail.com"
# password = "12345"
# import smtplib         # in this project import smtplit is not necessary 
# smtplib is a built-in Python module used to send emails using the Simple Mail Transfer Protocol (SMTP). It allows your Python scripts to send emails programmatically.
# The smtplib module provides an easy way to send emails using Python. It uses the SMTP protocol

email = input("Enter Gmail: ")
if "@" in email:   # "in" and "not in" is Membership operator
    #true
    password = input("Enter the password: ")
    if (email == "admin@gmail.com" and password == "12345"):
        print("You are successful login.")
    elif (email == "admin@gmail.com" and password != "12345"):
        print("Invalid password.")
        password = int(input("Enter again password: "))
        if (password == 12345):
            print("You are successful login.")
        else:
            print("Invalid password.")
    elif (email != "admin@gmail.com" and password == "12345"):
        print("Invalid email.")
        email = input("Enter again email: ")
        if (email == "admin@gmail.com" and password == "12345"):
            print("You are successful login.")
        else:
            print("Invalid email.")
    elif (email != "admin@gmail.com" and password != "12345"):
        print("Invalid email and password.")
        email = input("Enter again email: ")
        password = input("Enter again password: ")
        if (email == "admin@gmail.com" and password == "12345"):
            print("You are successful login.")
        else:
            print("Invalid email and password.")
else:
    # False
    print("Invalid email.")
