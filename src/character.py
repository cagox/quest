class AbilityScore:
    def __init__(self, score):
        self.score = score

    
    
class Character:
    def __init__(self, name="Hero"):
        self.name = name
		# MIND
        self.intelligence = AbilityScore(10)
        self.wisdom = AbilityScore(10)
        self.ego = AbilityScore(10)
        # BODY
        self.strength = AbilityScore(10)
        self.agility = AbilityScore(10)
        self.constitution = AbilityScore(10)
        # SPIRIT
        self.power = AbilityScore(10)
        self.gnosis = AbilityScore(10)
        self.quintessence = AbilityScore(10)
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