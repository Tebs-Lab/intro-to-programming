# Write a script that, when executed, allows the user to 
# play a game of rock paper scissors against a computer.
# To do this, you will need to accept input from the user,
# and use python's random module to control the computer's
# choices...

# Here is a little code to help you get started:

# This builtin function, choice, randomly selects an item from a list.
from random import choice
sample_list = ['a', 'b', 'c', 'd']



player_typed = input("Type something...\n> ")
print("Random selection: ", choice(sample_list))
print("Player typed: ", player_typed)
