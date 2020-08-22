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
