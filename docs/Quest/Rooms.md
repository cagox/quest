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