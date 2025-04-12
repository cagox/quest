"""
class Character holds the information specific to the character.
"""
from util import pad_after, money_string

class AbilityScore:
    """Holds and manipulates bility score values for the character."""
    def __init__(self, name="None", abbreviation="NON", score=10):
        self.__score = score
        self.name = name
        self.abbreviation = abbreviation

    def score(self):
        """returns the value of the ability score."""
        return self.__score

    def set_score(self, score):
        """sets the value of the ability score."""
        self.__score = score

    def modifier(self):
        """score()//5"""
        return self.score()//5

    def __repr__(self):
        return f"{self.name}: {self.score()}({self.modifier()})"

    def status_display(self):
        """This returns a string representation of the value made for the status screen."""
        space = 14
        score_string = f"{self.score()}(+{self.modifier()})"
        abbreviation_length = len(self.abbreviation)
        score_length = len(score_string)
        spaces = " " * (space-abbreviation_length-score_length)
        return f"{self.abbreviation}{spaces}{score_string}"


class Character:
    def __init__(self, name="Hero",
        	intelligence=10, wisdom=10, ego=10,
        	strength=10, agility=10, constitution=10,
        	power=10,gnosis=10,quintessence=10, copper=0, description="A Character.", location=None):
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
        self.copper = copper
        self.experience = 0
        self.spent_experience = 0
        self.description = description
        self.location = location

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

    def status_screen(self):
        print("\n")
        print("╔══════════════════════════════════════════════════╗")
        print(f"║ Name: {pad_after(self.name, " ", 42)} ║")
        print("╠════════════════╦═════════════════════════════════╣")
        exp = f"{self.experience:,}"
        cash = money_string(self.copper)
        print(f"║ EXP: {pad_after(exp," ",9)} ║ {pad_after(cash, " ",31)} ║")
        print("╠════════════════╬════════════════╦════════════════╣")
        print("║      MIND      ║      BODY      ║     SPIRIT     ║")
        print("╠════════════════╬════════════════╬════════════════╣")
        print(f"║ {self.intelligence.status_display()} ║ {self.strength.status_display()} ║ {self.power.status_display()} ║")
        print("╠════════════════╬════════════════╬════════════════╣")
        print(f"║ {self.wisdom.status_display()} ║ {self.agility.status_display()} ║ {self.gnosis.status_display()} ║")
        print("╠════════════════╬════════════════╬════════════════╣")
        print(f"║ {self.ego.status_display()} ║ {self.constitution.status_display()} ║ {self.quintessence.status_display()} ║")
        print("╠════════════════╬════════════════╬════════════════╣")
        hp = f"HP  {self.hitpoints}/{self.max_hitpoints()}"
        sp = f"SP  {self.stamina}/{self.max_stamina()}"
        ep = f"EP  {self.essence}/{self.max_essence()}"
        print(f"║ {pad_after(hp," ", 14)} ║ {pad_after(sp," ", 14)} ║ {pad_after(ep," ", 14)} ║")
        print("╚════════════════╩════════════════╩════════════════╝")
        print("\n")
    
    def say(self, message):
        print(f"{self.name} says \"{message.strip('"')}\"")
    
    def look(self):
        print(f"You see {self.name}.\n{self.description}")
    
    def move(self, destination):
        self.location = destination
        print(f"{self.name} moved to {destination.name}")
        self.location.visited = True
        self.location.look()

        
