file_object = open(r"File_name", "w")
with open('File_name', 'a') as file:
    file.write('Also a nice person\n')
file.close()
