"""
Quest:

Text Based Game by Cagox Media.

"""
from character import Character
from util import COPPER, SILVER, GOLD, PLATINUM


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
    hero.experience = 9999999

    hero.status_screen()


main()
