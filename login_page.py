import bcrypt


def hash_and_save_password(password, email):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    email = bcrypt.hashpw(email.encode('utf-8'), salt)
    # email = email.encode('utf-8')
    with open('user_credentials.txt', 'ab') as file:
        file.write(email + b" | " + hashed_password + b'\n')


def create_account(email):
    password = input("Create a new password: ")
    hash_and_save_password(password, email)
    option = input('Do you want to login? (Press Y for yes or q to quit): ')
    if option.lower() == 'q':
        quit()
    else:
        login(email)


def check_credentials(user_email, user_password, filename='user_credentials.txt'):
    with open(filename, 'rb') as file:
        for line in file:
            stored_email, stored_password = line.strip().split(b' | ')
            if bcrypt.checkpw(user_password.encode('utf-8'), stored_password) and bcrypt.checkpw(user_email.encode('utf-8'), stored_email):
            # if bcrypt.checkpw(user_password.encode('utf-8'), stored_password) and (user_email.encode('utf-8'), stored_email):
                return True
            # if user_email == stored_email and user_password == stored_password:
            #     return True
    return False


def login(email):
    count = 0
    while count < 3:
        password = input('Enter your password: ')
        if check_credentials(email, password) is True:
            print('Welcome to your account')
            quit()
        else:
            print('Incorrect password. Try Again!')
            count += 1
    else:
        print("You have provided an incorrect password multiple times! Please reset your password.")



def check_email_exists(email):
    with open('user_credentials.txt', 'rb') as file:
        for line in file:
            exist_email = line.strip().split(b' | ')
            if bcrypt.checkpw(email.encode('utf-8'), exist_email[0]):
                return True
    return False


def main():
    # print(key)
    print("Welcome to your Shift tracker.")
    email_add = input('Enter your Email address: ')
    if check_email_exists(email_add) is True:
        login(email_add)
    else:
        create_account(email_add)

main()
