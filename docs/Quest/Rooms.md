# Rooms

```python
class Exit:
	def __init__(self, destination, location):
		self.location = location # Room
		self.destination = destination # Room
```

```python
class Room:
	def __init__(self, description=None, outer_description=None, exits={}, contents=[]):
		self.description = description
		self.outer_description = outer_description
		self.exist = exits
		self.contents = contents

```

## About Rooms

Rooms are the locations that players can visit. They are containers that hold the players, exits, creatures, and any other objects that might exist in tghe world.

In this intial implementation I will be creating a grid of rooms, but the associated classes may be usable in other ways eventually as well, so I am not tying the room specific code to a grid. That will be handled by the World class.
