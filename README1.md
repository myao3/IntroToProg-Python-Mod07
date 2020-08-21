# Title
**Dev:** *Myao*   
**Date:** *8.20.2020*

### Name Error Handling (Try-Except)

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

### Name Error Handling (Try-Except)

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


![the result of NameError](https://github.com/myao3/IntroToProg-Python-Mod07/blob/master/docs/Assignment%2007-1-Answer.JPG "the Answer of NameError")
#### Figure 2. The result of the Answer of NameError

### Name Error Handling (Try-Except)

```
#------------------------------------------------- #
# Title: Pickle dump & Pickle Load1
# Description: A simple example of Pickle dump
# Chang.Log: (Who, When, What)
# Myao,08.19.2020
# ------------------------------------------------- #



import pickle
# Save a dictionary into a pickle file.
favorite_color = { "lion": "yellow", "kitty": "red" }
pickle.dump( favorite_color, open( "datafile2.txt", "wb" ) )

import pickle
# Load the dictionary back from the pickle file.
favorite_color = pickle.load( open("datafile2.txt", "rb" ) )
print(favorite_color)

#favorite_color is now { "lion": "yellow", "kitty": "red" }


```

#### Pickle dump & Pickle Load1


![the result of Pickle dump & Pickle Load1](https://github.com/myao3/IntroToProg-Python-Mod07/blob/master/docs/Assignment07-3-1.JPG "The result of Pickle dump & Pickle Load1")
#### Figure 3. The result of Pickle dump & Pickle Load1

### Name Error Handling (Try-Except)

```
#------------------------------------------------- #
# Title: Pickle dump & Pickle Load2
# Description: A simple example of Pickle dump
# Chang.Log: (Who, When, What)
# Myao,08.19.2020
# ------------------------------------------------- #



#favorite_color is now { "lion": "yellow", "kitty": "red" }
import pickle
stranimal = input("Enter a animal: ")
strcolor = input("Enter a color: ")
favorite_color = {stranimal: strcolor.strip()}

output = open("datafile2.txt", "ab")
pickle.dump(favorite_color, output)
output.close()

# Load the dictionary back from the pickle file.
with open("datafile2.txt", "rb") as f:
    favorite_color = pickle.load(f)
    print(favorite_color)
    favorite_color1 = pickle.load(f)
    print(favorite_color1)
#favorite_color is now { "lion": "yellow", "kitty": "red" }

```

#### Pickle dump & Pickle Load2


![the result of Pickle dump & Pickle Load2](https://github.com/myao3/IntroToProg-Python-Mod07/blob/master/docs/Assignment07-3-2.JPG "The result of Pickle dump & Pickle Load4")
#### Figure 4. The result of Pickle dump & Pickle Load2
