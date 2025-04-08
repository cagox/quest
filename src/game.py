"""
module game is where the game lives.
"""
from character import Character
from grammar import *
class Game:
    """
    class Game will be the driver of the whole thing. It will use the other classes to run the game.
    """
    def __init__(self, world, player, start_x=None, start_y=None):
        """
        max_x and max_y set the dimensions for the game world.
        """
        self.world = world
        self.player = player
        if start_x == None:
            self.player.location = self.world.get_room(self.world.min_x, self.world.min_y)
        else:
            self.player.location = self.world.get_room(start_x, start_y)
        self.interpreter = Interpreter(self)
        self.running = False
        
    def run(self):
        self.running = True
        self.player.location.look()
        command = ""
        while self.running: # != "!exit" and command != ":q":
            command = input("> ")
            self.interpreter.eval(command)
            
    
    def stop(self, message):
        print(message)
        self.running = False

class Interpreter:
    def __init__(self, game):
        self.game = game
    
    def eval(self, command):
        if len(command) == 0:
            return
        tokens = command.split() #Tokenize
        self.parse(tokens)
    
    def parse(self, tokens):
        verb = tokens[0]
        if len(tokens) == 1:
            if verb in QUIT:
                self.game.stop(f"Good bye! Invoked by {verb}")
                return
        if verb[0] == '"':
            self.game.player.say(" ".join(tokens))
            return
        if verb == "say":
            self.game.player.say(" ".join(tokens[1:])) 
            return
        if verb in self.game.player.location.exits.keys():
            self.game.player.move(self.game.player.location.exits[verb].destination)
            return
        if verb == "look":
            if len(tokens) == 1 or tokens[1] in HERE:
                self.game.player.location.look()
                return
            if tokens[1] == "me" or tokens[1] == "player":
                self.game.player.look()
                return
            if tokens[1] in self.game.player.location.exits.keys():
                self.game.player.location.exits[tokens[1]].destination.distant_look()
                return
            if len(tokens) > 2:
                if tokens[1] in AT:
                    if tokens[2] == "me" or tokens[2] == "player":
                        self.game.player.look()
                        return
                
        if verb in MOVE:
            target = None
            if len(tokens) == 2:
                target = tokens[1]
            if len(tokens) == 3 and tokens[2] in TO:
                target = tokens[2]
            if target == None:
                print("Where are you trying to go?")
                return
            exits = self.game.player.location.exits
            if target in exits:
                self.game.player.move(exits[target].destination)
                return
            print(f"You cannot go to {target}. It does not exits.")
            return
        print("I don't understand.")
        return
                