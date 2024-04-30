# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

play(player, quincy, 200)
play(player, abbey, 200)
play(player, kris, 200)
play(player, mrugesh, 200)

# Uncomment line below to play interactively against a bot:
play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
play(human, random_human, 200)