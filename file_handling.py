# file_object = open(r"File_name", "w")
# with open('File_name', 'a') as file:
#     file.write('Also a nice person\n')
# file.close()

with open('user_credentials.txt', 'r') as file:
    for line in file:
        exist_email = line.strip().split('|')
        print(exist_email[0])

