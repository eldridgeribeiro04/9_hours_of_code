"""Create a 'create account' page"""
import re

acc_holders = {}


def create_account():
    email = input("Enter your email: ")
    if email in acc_holders:
        print("You already have an account. Try logging in")
    else:
        password = input("Create a new password: ")
    acc_holders[email] = password
    with open('user_credentials.txt', 'w') as file:
        file.write(f"Email: {email}\n")
        file.write(f"Password: {password}\n")


def login():
    email = input("Enter your email address: ")
    if email in acc_holders:
        password = input("Enter your password: ")
        if acc_holders[email] == password:
            print("Welcome to your acount")
        else:
            input("You have entered a wrong password. Please try again!: ")

def main():
    print("Welcome to your Shift tracker.")
    choice = input("If you want to create an account, press 'E'."
                   "If you want to login, Press 'E'."
                   "Else, press 'q' to Quit: ")
    if choice.lower() == 'e':
        create_account()
    elif choice.lower() == "l":
        login()
    else:
        quit()



main()
