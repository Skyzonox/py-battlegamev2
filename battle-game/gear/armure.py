
class Armor:
    def __init__(self,name,defense,rarity) :
        self.name = name
        self.defense = defense
        self.rarity = rarity
        
    def defence(self, enemy):
        enemy.damage-= self.defence
    