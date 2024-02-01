import re


def create_account(email_add):
    email = email_add
    password = input("Create a new password: ")
    with open('user_credentials.txt', 'a') as file:
        file.write(email + '|' + password + '\n')
    option = input('Do you want to login? (Press Y for yes or q to quit: ')
    if option.lower() == 'y':
        login()
    else:
        quit()


def check_credentials(user_email, user_password, filename='user_credentials.txt'):
    with open('user_credentials.txt', 'r') as file:
        for line in file:
            stored_email, stored_password = line.strip().split('|')
            if user_email == stored_email and user_password == stored_password:
                return True
    return False


def login():
    email = input("Enter your email address: ")
    password = input('Enter your password: ')
    if check_credentials(email, password):
        print('Welcome to your account')
    else:
        option = input('Incorrect Email or password. Press enter to try again(Press q to quit:')
        if option.lower() != 'q':
            login()
        else:
            quit()


def main():
    print("Welcome to your Shift tracker.")

    email_add = input("Please enter your email: ")
    with open('user_credentials.txt', 'r') as file:
        credentials = file.readlines()

    for cred in credentials:
        if email_add in cred:
            print('This email already exists, please try a different email or use the login page!')
            option = input('Do you want to login?(Y for yes, N for no): ')
            if option.lower() == 'y':
                login()
        else:
            create_account(email_add)

main()
