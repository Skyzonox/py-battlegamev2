import random
from gear.weapon import Weapon
from gear.armure import Armor


class Orc:
    # Initialise les points de vie, nom arme et armure
    def __init__(self, name, health=250, attack_power=10,):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0
        
class Goblin:
    # Initialise les points de vie, nom arme et armure
    def __init__(self, name, health=100, attack_power=5 ):
        self.name =name
        self.health=health
        self.attack_power=attack_power
        
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0
    
class Cyclope:
    # Initialise les points de vie, nom arme et armure
    def __init__(self, name, health=150, attack_power=20 ):
        self.name =name
        self.health=health
        self.attack_power=attack_power
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0
    
class Minotaure:
    # Initialise les points de vie, nom arme et armure
    def __init__(self, name, health=100, attack_power=30 ):
        self.name =name
        self.health=health
        self.attack_power=attack_power
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0

# boss
class Smaug:
    # Initialise les points de vie, nom arme et armure
    def __init__(self, name, health=500, attack_power=50):
        self.name =name
        self.health=health
        self.attack_power=attack_power
        
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0
