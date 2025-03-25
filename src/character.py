class AbilityScore:
    def __init__(self, name="None", abbreviation="NON", score=10):
        self.__score = score
        self.name = name
        self.abbreviation = abbreviation

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
		self.intelligence = AbilityScore(name="Intelligence", score=intelligence, abbreviation="INT")
		self.wisdom = AbilityScore(name="Wisdom", score=wisdom, abbreviation="WIS")
		self.ego = AbilityScore(name="Ego", score=ego, abbreviation="EGO")
		# BODY
		self.strength = AbilityScore(name="Strength", score=strength, abbreviation="STR")
		self.agility = AbilityScore(name="Ability", score=agility, abbreviation="AGI")
		self.constitution = AbilityScore(name="Constitution", score=constitution, abbreviation="CON")
		# SPIRIT
		self.power = AbilityScore(name="Power", score=power, abbreviation="POW")
		self.gnosis = AbilityScore(name="Gnosis", score=gnosis, abbreviation="GNO")
		self.quintessence = AbilityScore(name="Quintessence", score=quintessence, abbreviation="QUINT")
		# Now that we have the functions for derived attributes,
		# we can set the values in the class.
		self.hitpoints = self.max_hitpoints()
		self.stamina = self.max_stamina()
		self.essence = self.max_essence()
		self.copper = 0
		
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
	