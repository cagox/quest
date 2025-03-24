class AbilityScore:
    def __init__(self, name="None", score=10):
        self.__score = score
        self.name = name

    def score(self):
        return self.__score
    
    def set_score(self, score):
        self.__score = score
    
    def modifier(self):
        return self.score//5
    
    def __repr__(self):
        return f"{self.name}: {self.score()}({self.modifier()})"

    
    
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
		return self.ego.score() + self.constitution.score() +  self.quintessence.score()
			
	def mana(self):
		return self.quintessence.score()
		
	def max_essence(self):
		#Essence = Ego + Mana
		return self.ego.score() + self.mana()
		
	def max_stamina(self):
		# Stamina = Ego + Constitution
		return self.ego.score() + self.constitution.score()
		
	def __repr__(self):
	    return f"{self.name} is a Character with {self.hitpoints} hitpoints." 
	