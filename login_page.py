import re


def create_account(email):
    password = input("Create a new password: ")
    with open('user_credentials.txt', 'a') as file:
        file.write(email + '|' + password + '\n')
    option = input('Do you want to login? (Press Y for yes or q to quit): ')
    if option.lower() == 'q':
        quit()
    else:
        login(email)
#
#
def check_credentials(user_email, user_password, filename='user_credentials.txt'):
    with open('user_credentials.txt', 'r') as file:
        for line in file:
            stored_email, stored_password = line.strip().split('|')
            if user_email == stored_email and user_password == stored_password:
                return True
    return False


def login(email):
    password = input('Enter your password: ')
    if check_credentials(email, password) is True:
        print('Welcome to your account')
    else:
        option = input('Incorrect Email or password. Press enter to try again(Press q to quit):')
        if option.lower() == 'q':
            quit()
        else:
            login()


def check_email_exists(email):
    with open('user_credentials.txt', 'r') as file:
        for line in file:
            exist_email = line.strip().split()
            if email[0] == exist_email:
                return True
    return False

def main():
    print("Welcome to your Shift tracker.")
    email_add = input('Enter your Email address: ')
    if check_email_exists(email_add):
        option = input("User exists, if you would like to login type 'l' (type q to quit): ")
        if option.lower() == 'q':
            quit()
        else:
            login(email_add)
    else:
        create_account(email_add)

main()
