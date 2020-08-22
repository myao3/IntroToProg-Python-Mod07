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
