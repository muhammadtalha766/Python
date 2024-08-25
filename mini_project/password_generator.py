import random
char = "aquickbrownfoxjumpsoverthelazydog1234567890!@#$%"
password = ""
length = int(input("Enter length: "))
for a in range (length):
    password += random.choice(char)
print (password)