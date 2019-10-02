# Write a script that, when executed, allows the user to 
# play a game of rock paper scissors against a computer.
# To do this, you will need to accept input from the user,
# and use python's random module to control the computer's
# choices...

# Here is a little code to help you get started:

# This builtin function, choice, randomly selects an item from a list.
from random import choice

# For strings that you use repeatedly, it's a common best practice to 
# define them once, then use the variables. This reduces errors from typos
# and makes things easier to change in the future (e.g. capitalizing Rock Paper Scissors...)
rock = 'rock'
paper = 'paper'
scissors = 'scissors'
choices = [rock, paper, scissors]

player_choice = None
while player_choice == None:
    player_choice = input("Do you throw rock, paper, or scissors?\n> ")
    if player_choice not in choices:
        print(f'Sorry, you must type rock, paper, or scissors EXACTLY. You typed: {player_choice}\n')
        player_choice = None

computer_choice = choice(choices)

# To save some typing, I stored all the messages in variables. 
loss = "You lost."
win = "You win!"
draw = "It's a tie..."
error = "This message should not be displayed... is the game broken?"
outcome_message = None

# This nested if/else block is annoying to write...
# but sometimes you just have to encode the rules.
if player_choice == computer_choice:
    outcome_message = draw
elif player_choice == rock:
    if computer_choice == paper:
        outcome_message = loss
    elif computer_choice == scissors:
        outcome_message = win
    else:
        outcome_message = error
elif player_choice == paper:
    if computer_choice == rock:
        outcome_message = win
    elif computer_choice == scissors:
        outcome_message = loss
    else:
        outcome_message = error
elif player_choice == scissors:
    if computer_choice == rock:
        outcome_message = loss
    elif computer_choice == paper:
        outcome_message = win
    else:
        outcome_message = error
else:
    outcome_message == error

# Okay great, now just print the messages!
print(f'You chose: {player_choice}. Computer chose: {computer_choice}... {outcome_message}')
