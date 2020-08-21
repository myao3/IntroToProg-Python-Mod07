# Title
**Dev:** *Myao*   
**Date:** *8.20.2020*

## Name Error Handling (Try-Except)When you are programming, you fix your bugs immediately and make sure the code runs smoothly. However, it often happens that other people introduce new bugs when they use your program.### Raising Custom ErrorsPython automatically generates errors based on conditions defined by the Python Runtime. However, you can also "raise" errors based on custom conditions . 

```
# ------------------------------------------------- #
# Title: NameError
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
    print(read_file_data_to_list(file_name=strfile))   # causes an error if call unexist name
except ZeroDivisionError as e:
    print("Please do no use Zero for the second number!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

except NameError as e:
    print("A local or global name is not found!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
    
```
#### NameError


![the result of NameError](https://github.com/myao3/IntroToProg-Python-Mod07/blob/master/docs/Assignment%2007-1-1.JPG "the result of NameError")
#### Figure 1. The result of NameError

