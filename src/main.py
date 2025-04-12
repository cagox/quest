"""
Quest:

Text Based Game by Cagox Media.

"""
from character import Character
from util import COPPER, SILVER, GOLD, PLATINUM
from game import Game
from room import Room
from world import World
from descriptions import decorate

def main():
    """So far just playing around."""
    elf = {
        'intelligence': 15,
        'ego': 15,
        'agility': 20,
        'power': 15,
        'quintessence': 20,
        'copper': (16*COPPER + 11*SILVER + 2*GOLD + 1*PLATINUM),
    }
    hero = Character("Hero", **elf)   
    game = Game(World(), hero)
    game.world.build_maze()
    decorate(game)
    game.run()

main()


# TODO: Have "fold_desciption" check to see if a description is empty.
# TODO: Have Make sure fold description is folding at the right time. 
#       I saw an edge case that moved the border.
