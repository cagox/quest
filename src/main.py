def main():
    hero = Character("Hero", "Adventurer", 35)

    print(hero)

class Character:
    def __init__(self, name, character_class, hitpoints):
        self.name = name
        self.character_class = character_class
        self.hitpoints = hitpoints
    
    def __repr__(self):
        return f"{self.name} is a member of the {self.character_class} class, and has {self.hitpoints} hitpoints."

main()
