from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

password = f.encrypt(b'Eldridge')
password = password.decode()
print(password)

dec_pw = f.decrypt(password)
print(dec_pw.decode())
