# ------------------------------------------------- #
# Title: the Answer of NameError
# Description: A try-catch with multiple error messages
# https://docs.python.org/3/library/exceptions.html#bltin-exceptions
# ChangeLog: (Who, When, What)
# myao,8.18.2020,Created Script
# ------------------------------------------------- #
names = 'bob\nsue'
nameoffile = 'SomeFile.txt'

def save_data(data, file_name):
        f = open(file_name, 'w+')
        f.write(data+'\n')
        f.close()

save_data(data=names, file_name=nameoffile)

def read_file_data_to_list(file_name):
    f = open(file_name, 'r')
    data = f.readlines()  # reads rows of data into a list object
    f.close()
    return data
try:
    print(read_file_data_to_list(file_name=nameoffile))   # causes an error if call unexist name
except NameError as e:
    print("A local or global name is not found!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except FileNotFoundError as e:
    print("Text file must exist before running this script!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
