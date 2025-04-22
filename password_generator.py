import random
import string
digits = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_chars = "!@#$%^&*"
#input
include_digits = input ("Welcome to password generator !")
include_digits = input("Do you want digits in your password? (yes/no): ").lower() == "yes"
include_letters = input("Do you want letters in your password? (yes/no): ").lower() == "yes"
include_special = input("Do you want special characters in your password? (yes/no): ").lower() == "yes"


pool = ""
if include_digits:
    pool += digits
if include_letters:
    pool += letters
if include_special:
    pool += special_chars
length = int(input("Enter the password lenght: "))
password = ''.join(random.choice(pool) for _ in range(length))
print("Your password is: "+password)  
       
include_digits = input(" Thankyou for using our code ") 
include_digits = input(" Visit Again ! ") 
