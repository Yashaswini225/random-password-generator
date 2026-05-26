# Account Creation with Random Password Generator

import random

# Characters used for password generation
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"

print("=== Create Account ===")

# Ask user for username
username = input("Enter username: ")

# Ask user for password choice
choice = input("Do you want a random password? (yes/no): ")

# Generate random password of fixed size 8
if choice.lower() == "yes":

    password = ""

    for i in range(8):
        password += random.choice(chars)

    print("Generated Password:", password)

# User enters own password
else:
    password = input("Enter your password: ")

# Save account details
file = open("CreatedAccounts.txt", "a")

file.write(f"Username: {username}, Password: {password}\n")

file.close()

print("Account created successfully!")