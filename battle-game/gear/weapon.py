class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self, enemy):
        enemy.hp -= self.damage  
        print(f"{enemy.name} reçoit {self.damage} dégâts avec {self.name}.")

    def __str__(self):
        return f"Weapon: {self.name}, Damage: {self.damage}"


class Magic:
    def __init__(self, name, damage, mana, drop):
        self.name = name
        self.damage = damage
        self.mana = mana
        self.drop = drop

    def attack(self, enemy):
        enemy.hp -= self.damage
        print(f"{enemy.name} reçoit {self.damage} dégâts avec le sort {self.name}.")

    def __str__(self):
        return f"Magic: {self.name}, Damage: {self.damage}, Mana: {self.mana}, Drop: {self.drop}"


class Spell:
    def __init__(self, name, damage, mana):
        self.name = name
        self.damage = damage
        self.mana = mana  

    def attack(self, enemy):
        enemy.hp -= self.damage
        print(f"{enemy.name} reçoit {self.damage} dégâts avec le sort {self.name}.")

    def __str__(self):
        return f"Spell: {self.name}, Damage: {self.damage}, Mana Cost: {self.mana}"


def perform_attack(attacker, defender):
    print(f"\n{attacker.name} attaque {defender.name}!")
    
    damage = attacker.weapon.damage  

    if isinstance(attacker, Wizzard):
        if attacker.mana > 0:
            print(f"Vous avez {attacker.mana} mana.")
            print("1. Attaque normale")
            print(f"2. Utiliser un sort (Coût : {attacker.spell.mana} mana)")
            
            choice = input("Choisissez votre attaque (1-2) : ")
            while choice not in ["1", "2"]:
                print("Choix invalide.")
                choice = input("Choisissez votre attaque (1-2) : ")
            
            if choice == "2":
                if attacker.mana >= attacker.spell.mana:
                    attacker.mana -= attacker.spell.mana  
                    damage = attacker.spell.damage
                    attacker.spell.attack(defender)
                    print(f"Sort utilisé : {attacker.spell.name}, dégâts : {damage}. Mana restant : {attacker.mana}")
                else:
                    print("Mana insuffisant! Attaque normale effectuée.")
        else:
            print("Mana épuisé! L'attaque normale est utilisée automatiquement.")
    
    if choice != "2" or attacker.mana < attacker.spell.mana:
        attacker.weapon.attack(defender)
    
    print(f"Points de vie restants pour {defender.name}: {max(defender.hp, 0)} PV.")



class Wizzard:
    def __init__(self, name, hp, weapon, armor, mana, level, spell):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
        self.mana = mana
        self.level = level
        self.spell = spell

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_armor(self, armor):
        self.armor = armor


class Barbarian:
    def __init__(self, name, hp, weapon, armor):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_armor(self, armor):
        self.armor = armor
