import random
from collections import Counter


# Define a function to generate the next move based on opponent's move history
def predict_opponent_move(opponent_history):
    # Analyze opponent's move history to find patterns
    if len(opponent_history) >= 3:
        # Check if the opponent frequently repeats the same move
        if opponent_history[-1] == opponent_history[-2] and opponent_history[-2] == opponent_history[-3]:
            return counter_move(opponent_history[-1])  # Counter the repeated move
        # Check if the opponent has a tendency to follow a certain pattern
        elif opponent_history[-1] == counter_move(opponent_history[-2]):
            return counter_move(opponent_history[-1])  # Counter the expected next move
        # Check if the opponent has a tendency to play the same move after losing
        elif len(opponent_history) >= 4 and opponent_history[-1] == counter_move(opponent_history[-4]):
            return counter_move(opponent_history[-1])  # Counter the expected next move
    # If no clear pattern is detected, predict the move that defeats the most frequent opponent move
    return random.choice(["R", "P", "S"])

# Define a function to determine the counter move
def counter_move(move):
    if move == "R":
        return "S"  # Paper beats Rock
    elif move == "P":
        return "R"  # Scissors beat Paper
    else:
        return "P"  # Rock beats Scissors

# Define the player function
def player(prev_play, opponent_history=[]):
    # If this is the first game in a match, reset opponent's history
    if prev_play == "":
        opponent_history = []
    
    # Determine opponent's last move
    if opponent_history:
        opponent_last_move = opponent_history[-1]
    else:
        opponent_last_move = ""
    
    # Predict opponent's next move and counter it
    opponent_next_move = predict_opponent_move(opponent_history)
    return counter_move(opponent_next_move)

 # Example call to player function with previous play and opponent's history