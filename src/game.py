"""
module game is where the game lives.
"""
from character import Character

class Game:
    """
    class Game will be the driver of the whole thing. It will use the other classes to run the game.
    """
    def __init__(self, max_x, max_y, player, start_room):
        """
        max_x and max_y set the dimensions for the game world.
        """
        self._max_x = max_x
        self._max_y = max_y
        self.player = player
        player.location = start_room
        
    def run(self):
        self.player.location.status()
        command = ""
        while command != "!exit" and command != ":q":
            command = input("> ")
        print("Good bye!")
    