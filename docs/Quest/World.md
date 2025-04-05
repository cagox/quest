```python
from rooms import Room
	def __inti__(self, min_x=-5, min_y=-5, max_x=5, max_y=5, 
					seen=False, visited=False):
		self.min_x = min_x
		self.min_y = min_y
		self.max_x = max_x
		self.max_y = max_y
		self.grid = [[Room() for i in range(self.cols())] for j in range(self.rows())]
		self.seen = seen
		self.visited = visited
	
	def rows(self):
		return (max_y - min_y)
	def cols(self):
		return (max_x - min_x)
		
	# These might not end up being used.
	def grid_x(self, world_x):
		return world_x + (0 - self.min_x)
	def grid_y(self, world_y):
		return world_y + (0 - self.min_y)
```

## The World
The world is a grid of Room objects. Each room object has a "seen" and a visited member variable. These can be used for creating maps and such.

