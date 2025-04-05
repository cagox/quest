```python
class Character:
	def __init__(self, name="Hero",
			intelligence=10, wisdom=10, ego=10,
			strength=10, agility=10, constitution=10,
			power=10,gnosis=10,quintessence=10):
		self.name = name
		# MIND
		self.intelligence = AbilityScore("Intelligence", intelligence)
		self.wisdom = AbilityScore("Wisdom", wisdom)
		self.ego = AbilityScore("Ego", ego)
		# BODY
		self.strength = AbilityScore("Strength", strength)
		self.agility = AbilityScore("Ability", agility)
		self.constitution = AbilityScore("Constitution", constitution)
		# SPIRIT
		self.power = AbilityScore("Power", power)
		self.gnosis = AbilityScore("Gnosis", gnosis)
		self.quintessence = AbilityScore("Quintessence", quintessence)
		# Now that we have the functions for derived attributes,
		# we can set the values in the class.
		self.hitpoints = self.max_hitpoints()
		self.stamina = self.max_stamina()
		self.essence = self.max_essence()

	def max_hitpoints(self):
        # Hit Points = Ego +  Constitution + Quintessence
        return self.ego.score + self.constitution.score + self.quintessence.score

	def mana(self):
		return self.quintessence.score
        
	def max_essence(self):
		#Essence    = Ego + Mana
        return self.ego.score + self.mana()
        
	def max_stamina(self):
		# Stamina = Ego + Constitution
		return self.ego.score + self.constitution.score 
	
	def __repr__(self):
		return f"{self.name} is a Character with {self.hitpoints} hitpoints."
		#This function will help keep our current main() working.
```

```python
class AbilityScore:
	def __init__(self, name, score=10):
		self.score = score
		self.name = name
		
	def modifier(self):
		return self.score//5
		
	def __repr__(self):
		return f"{self.name}: {self.score} ({self.modifier()})"
```
## The Character
This class is likely to change a lot. It might end up being entirely restructured anyway. A lot depends on how I eventually end up deciding to handle races, and monsters and such.

For now I am creating the character with basic stats that will be used later down the road once other features are implemented.
