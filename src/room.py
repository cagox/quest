from util import pad_after
class Exit:
    """
    class Exit:
    Exits move between rooms.
    """
    def __init__(self, destination, location):
        """
        destination is the room you are going to.
        location is the room the door is in.        
        """
        self.location = location # Room
        self.destination = destination # Room
        
class Room:
    def __init__(self, name="A Room", description=None, outer_description=None, exits={}, contents=[]):
        self.name = name
        self.description = description
        self.outer_description = outer_description
        self.exits = exits
        self.contents = contents
        
    def add_exit(self, name, destination, return_name):
        self.exits[name] = Exit(destination, self)
        destination.exits[return_name] = Exit(self, destination)
    
    def status(self):
        print("╔══════════════════════════════════════════════════╗")
        print(f"║ {pad_after(self.name, " ",48)} ║")
        print("╠══════════════════════════════════════════════════╣")
        self.fold_description(self.description, 48)
        print("╚══════════════════════════════════════════════════╝")
        
    def fold_description(self, description, length):
        if len(description) <= length:
            print(f"║ {pad_after(description, " ",length)} ║")
            return
        tokens = description.split()
        string = tokens[0]
        tokens.pop(0)
        while len(string) + len(tokens[0]) <= length and len(tokens) > 0:
            string += f" {tokens[0]}"
            tokens.pop(0)

        print(f"║ {pad_after(string, " ", 48)} ║")
        if len(tokens) > 0:
            string = " ".join(tokens)
            self.fold_description(string, length)
        

