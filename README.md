# IntroToProg-Python-Mod07
**Dev:** *Myao*   
**Date:** *8.20.2020*

### In Structured error handling function, I write “print(read_file_data_to_list(file_name=strfile (file_name=strfile)) under “try”; and write three exceptions: ZeroDivisionError, NameError, Exception. “strfile” is the wrong name and causing the error. The script will display the exception and run its error message. ZeroDivisionError is not the corrected exception  and NameError is the correct exception and run its error message. 

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


![the result of NameError](https://github.com/myao3/IntroToProg-Python-Mod07/blob/master/docs/Assignment%2007-1-1%20result.JPG "the result of NameError")
#### Figure 1. The result of NameError 

```
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
    
```

#### the Answer of NameError


![the result of NameError](https://github.com/myao3/IntroToProg-Python-Mod07/blob/master/docs/Assignment%2007-1-1%20answer.JPG "the Answer of NameError")
#### Figure 2. The result of the Answer of NameError in txt.file

### In Structured error handling function, I write “result = x/y under “try”; and write three exceptions: NameError, ZeroDivisionError. I run the function with zero; this is causing the ZeroDivisionError and run its error message. If I run the function without zero, the script display the result with no exception. 

```
# ------------------------------------------------- #
# Title: zerodivisionerror
# Description: A try-catch with one error message
# https://docs.python.org/3/library/exceptions.html#bltin-exceptions
# ChangeLog: (Who, When, What)
# myao,8.18.2020,Created Script
# ------------------------------------------------- #


def divide(x, y):
    try:
        result = x / y
    except NameError as e:
        print("A local or global name is not found!")
        print(e, e.__doc__, type(e), sep='\n')
    except ZeroDivisionError as e:
        print("division by zero!")
    else:
        print("result is", result)

divide(2, 0)
divide(2, 1)

```
![the result of zerodivisionerror](https://github.com/myao3/IntroToProg-Python-Mod07/blob/master/docs/Assignment%2007-1-2%20result.JPG "The result of zerodivisionerror")
#### Figure 3. The result of zerodivisionerror


### For the below script, I use pickle.dump(data, txt.file) to save data to a pickle file and use pickle.load(data, txt.file) to load data. 

```
#------------------------------------------------- #
# Title: Pickle dump & Pickle Load1
# Description: A simple example of Pickle dump
# Chang.Log: (Who, When, What)
# Myao,08.19.2020
# ------------------------------------------------- #



import pickle
# Save a dictionary into a pickle file.
favorite_color = { "Cat": "black", "elephant": "grey" }
pickle.dump( favorite_color, open( "datafile2.txt", "wb" ) )

# Load the dictionary back from the pickle file.
favorite_color = pickle.load( open("datafile2.txt", "rb" ) )
print(favorite_color)

#favorite_color is now { "Cat": "black", "elephant": "grey" }

```

#### Pickle dump & Pickle Load1

![the result of Pickle dump & Pickle Load1](https://github.com/myao3/IntroToProg-Python-Mod07/blob/master/docs/Assignment%2007-3-1%20result.JPG "The result of Pickle dump & Pickle Load1")
#### Figure 4. The result of Pickle dump & Pickle Load1

### For the below script, I use pickle.dump(data, txt.file) to append user input data to a pickle file and use pickle.load(data, txt.file) to load all data from txt.file. 

```
#------------------------------------------------- #
# Title: Pickle dump & Pickle Load2
# Description: A simple example of Pickle dump
# Chang.Log: (Who, When, What)
# Myao,08.19.2020
# ------------------------------------------------- #


import pickle
stranimal = input("Enter a animal: ")
strcolor = input("Enter a color: ")
favorite_color = {stranimal: strcolor.strip()}

output = open("datafile2.txt", "ab")
pickle.dump(favorite_color, output)
output.close()


with open("datafile2.txt", "rb") as f:
    favorite_color = pickle.load(f)
    print(favorite_color)
    favorite_color1 = pickle.load(f)
    print(favorite_color1)
```
#### Pickle dump & Pickle Load2

![the result of Pickle dump & Pickle Load2](https://github.com/myao3/IntroToProg-Python-Mod07/blob/master/docs/Assignment%2007-3-2%20result.JPG "The result of Pickle dump & Pickle Load2")
#### Figure 5. The result of Pickle dump & Pickle Load2

#### the result of Pickle dump & Pickle Load2 in txt.file

![the result of Pickle dump & Pickle Load2 in txt.file](https://github.com/myao3/IntroToProg-Python-Mod07/blob/master/docs/Assignment%2007-3-2%20result%20txt.JPG "the result of Pickle dump & Pickle Load2 in txt.file")
#### Figure 6. the result of Pickle dump & Pickle Load2 in txt.file

