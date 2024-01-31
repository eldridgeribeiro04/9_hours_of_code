"""Create a 'create account' page"""
import re

acc_holders = {}


# def create_account():
#     email = input("Enter your email: ")
#     if email in acc_holders:
#         print("You already have an account. Try logging in")
#     else:
#         password = input("Create a new password: ")
#     acc_holders[email] = password
#     with open('user_credentials.txt', 'a') as file:
#         file.write(email | password)
#
#
#
# def login():
#     email = input("Enter your email address: ")
#     if email in acc_holders:
#         password = input("Enter your password: ")
#         if acc_holders[email] == password:
#             print("Welcome to your acount")
#         else:
#             input("You have entered a wrong password. Please try again!: ")
#     else:
#         print("User does not exist. Create an account.")

def main():
    print("Welcome to your Shift tracker.")
    # choice = input("If you want to create an account, press 'E'."
    #                "If you want to login, Press 'E'."
    #                "Else, press 'q' to Quit: ")

    email = input("Please enter your email: ")
    with open('user_credentials.txt', 'r') as file:
        credentials = file.readlines()

    for cred in credentials:
        if email in any(cred):
            print('This works')
        else:
            print('Fuck off')



main()
