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
    
    #long_description = "You are in a glorious room full of wonderful stuff. "
    #long_description += "I am sure this description will go over and have to be wrapped. "
     
    
    #start_room = Room("The Beginning", long_description, "The Starting Room is through that door.")
    #second_room = Room("The End", "You are in the second room.", "The second room is through that door.")
    
    #start_room.add_exit_and_return("north", second_room, "south")
    # second_room.add_exit("south", start_room)
    
    game = Game(World(), hero)
    game.world.build_maze()
    decorate(game)
    game.run()

main()
