# Modification pour barbarian.py
class Barbarian:
    def __init__(self, name, hp, weapon, armor):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor

    def attack(self, enemy):
        # Attaque 1
        damage = self.weapon.damage
        if enemy.armor and enemy.armor.defense > 0:
            enemy.armor.defense -= damage
            if enemy.armor.defense < 0:
                enemy.hp += enemy.armor.defense  # Dégâts restants affectent les HP
                enemy.armor.defense = 0
            print(f"{self.name} attaque {enemy.name} et inflige {damage} dégâts à l'armure!")
            print(f"Il reste {enemy.armor.defense} points d'armure à {enemy.name}")
        else:
            enemy.hp -= damage
            print(f"{self.name} attaque {enemy.name} et inflige {damage} dégâts!")
            print(f"Il reste {enemy.hp} HP à {enemy.name}")
        
        # Attaque 2 (Le barbare attaque deux fois)
        if enemy.hp > 0:  # Vérifier si l'ennemi est encore vivant
            damage = self.weapon.damage
            if enemy.armor and enemy.armor.defense > 0:
                enemy.armor.defense -= damage
                if enemy.armor.defense < 0:
                    enemy.hp += enemy.armor.defense
                    enemy.armor.defense = 0
                print(f"{self.name} attaque encore {enemy.name} et inflige {damage} dégâts à l'armure!")
                print(f"Il reste {enemy.armor.defense} points d'armure à {enemy.name}")
            else:
                enemy.hp -= damage
                print(f"{self.name} attaque encore {enemy.name} et inflige {damage} dégâts!")
                print(f"Il reste {enemy.hp} HP à {enemy.name}")

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_armor(self, armor):
        self.armor = armor