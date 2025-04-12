
from room import Room
import random

class World:
    def __init__(self, min_x=-5, min_y=-5, max_x=5, max_y=5):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.grid = [[Room() for i in range(self.cols())] for j in range(self.rows())]
    
    def rows(self):
        return (self.max_y - self.min_y)
    
    def cols(self):
        return (self.max_x - self.min_x)
    
    def grid_x(self, world_x):
        return world_x + (0 - self.min_x)
    def grid_y(self, world_y):
        return world_y + (0 - self.min_y)
    def get_room(self, x, y):
        return self.grid[self.grid_x(x)][self.grid_y(y)]
    
    def build_maze(self):
        self.visit_rooms_r(self.min_x, self.min_y)
        self.reset_rooms_visited()
        self.decorate_rooms()
    
    def visit_rooms_r(self, x, y):
        self.get_room(x,y).visited = True
        
        while True:
            next_index_list = []
            # West
            if x > self.min_x and not self.get_room(x-1,y).visited:
                next_index_list.append((x-1,y))
            # East
            if x < self.max_x - 1 and not self.get_room(x+1, y).visited:
                next_index_list.append((x+1,y))
            # North
            if y > self.min_y and not self.get_room(x, y-1).visited:
                next_index_list.append((x, y-1))
            # South
            if y < self.max_y-1 and not self.get_room(x, y+1).visited:
               next_index_list.append((x,y+1))             

            # If no path, break
            if len(next_index_list) == 0:
                return
            
            #Randomly choose next  direction to go.
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list.pop(direction_index)
            
            new_x, new_y = next_index[0], next_index[1]
            current_room = self.get_room(x,y)
            next_room = self.get_room(new_x, new_y)
            
            #Make doors
            # East
            if new_x == x+1:
                current_room.add_exit_and_return("east", next_room, "west")
            # West
            if new_x == x-1:
                current_room.add_exit_and_return("west", next_room, "east")
            # South
            if new_y == y+1:
                current_room.add_exit_and_return("south", next_room, "north")
            # North
            if new_y == y-1:
                current_room.add_exit_and_return("north", next_room, "south")
            
            # recursively visit next room
            self.visit_rooms_r(new_x, new_y)

    def reset_rooms_visited(self):
        for x in range(self.cols()):
            for y in range(self.rows()):
                self.grid[x][y].visited = False
    
    def decorate_rooms(self):
        # TODO: Add this code.
        pass
    
    def draw_map(self,player_location):
        for y in range(self.rows()):
            row1 = ""
            row2 = ""
            row3 = ""
            for x in range(self.cols()):
                room = self.grid[x][y]
                if room == player_location:
                    rowA, rowB, rowC = room.map_image(True)
                else:
                    rowA, rowB, rowC = room.map_image(False)
                row1 = f"{row1}{rowA}"
                row2 = f"{row2}{rowB}"
                row3 = f"{row3}{rowC}"
            print(f"{row1}\n{row2}\n{row3}")