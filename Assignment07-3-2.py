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
