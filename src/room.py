from util import pad_after

ROOMNOTDESCRIBED = "You see a place with no description."

class Exit:
    """
    class Exit:
    Exits move between rooms.
    """
    def __init__(self, destination):
        """
        destination is the room you are going to.
        location is the room the door is in.        
        """
        self.destination = destination # Room
        
class Room:
    def __init__(self, name="A Room", description=ROOMNOTDESCRIBED, outer_description=ROOMNOTDESCRIBED, contents=[], visited=False, seen=False):
        self.name = name
        self.description = description
        self.outer_description = outer_description
        self.exits = {}
        self.contents = contents
        self.visited = visited
        self.seen = seen
        
    def add_exit(self, name, destination):
        self.exits[name] = Exit(destination)
    
    def add_exit_and_return(self, name, destination, return_name):
        self.add_exit(name, destination)
        destination.add_exit(return_name, self)
    
    def look(self):
        print("╔══════════════════════════════════════════════════╗")
        print(f"║ {pad_after(self.name, " ",48)} ║")
        print("╠══════════════════════════════════════════════════╣")
        self.fold_description(self.description, 48)
        print("╠══════════════════════════════════════════════════╣")
        if len(self.exist_string()) <= 48:
            print(f"║ {pad_after(self.exist_string(), " ", 48)} ║")
        else:
            self.fold_description(self.exist_string(), 48)
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
            
    def exist_string(self):
        exits = self.exits.keys()
        exitstring = "Exits:"
        if len(exits) == 0:
            return f"{exitstring} No Exits"
        for key in exits:
            exitstring = f"{exitstring} {key}"
        return exitstring
    
    def distant_look(self):
        print(f"You see {self.name}: {self.outer_description}")

