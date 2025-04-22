import random
import string
print(r"""
  _____                                    _    
 |  __ \                                  | |   
 | |__) |_ _ ___ _____      _____  _ __ __| |   
 |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |   
 | |  | (_| \__ \__ \\ V  V / (_) | | | (_| | 
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|   
                                 | |            
   __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
   __/ |                                        
  |___/               
  
  Password generator by Sai and Arnik
                            
""")

digits = "0123456789"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_chars = "!@#$%^&*"
#input
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

