# Telemarketer.py
# ICS201 Jeel Vekaria
# Feb 12, 2020
 
print("Enter number based on last 4 digits of your phone number")
n=int(input("Enter first digit of your number:"))
n2=int(input("Enter second digit of your number:"))
n3=int(input("Enter third digit of your number:"))
n4=int(input("Enter fourth digit of your number:"))

if n==8 or n==9 and n2==n3 and n4==8 or n4==9:
    print("Decline")
else:
    print("Answer")