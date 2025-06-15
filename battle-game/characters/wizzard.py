from characters.barbarian import Barbarian
import random

class Wizzard:
    def __init__(self, name, hp, weapon, armor, mana, level, spell):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
        self.mana = mana
        self.level = level
        self.spell = spell

    def attack(self, enemy):
        # Si en mode interactif (joueur)
        if hasattr(enemy, 'is_player') or isinstance(enemy, Barbarian):
            print(f"Vous avez {self.mana} mana.")
            print("1. Attaque normale avec l'arme")
            if self.mana >= self.spell.mana:
                print(f"2. Utiliser un sort (Coût: {self.spell.mana} mana)")
                choice = input("Choisissez votre attaque (1-2): ")
            else:
                print("Vous n'avez pas assez de mana pour lancer un sort.")
                choice = "1"
                
            if choice == "2" and self.mana >= self.spell.mana:
                damage = self.spell.damage
                self.mana -= self.spell.mana
                print(f"{self.name} lance {self.spell.name} sur {enemy.name} et inflige {damage} dégâts!")
                print(f"Il vous reste {self.mana} mana.")
            else:
                damage = self.weapon.damage
                print(f"{self.name} attaque {enemy.name} avec {self.weapon.name} et inflige {damage} dégâts!")
        else:
            # Si IA (ennemi)
            if self.mana >= self.spell.mana and random.randint(1, 2) == 2:
                damage = self.spell.damage
                self.mana -= self.spell.mana
                print(f"{self.name} lance {self.spell.name} sur {enemy.name} et inflige {damage} dégâts!")
            else:
                damage = self.weapon.damage
                print(f"{self.name} attaque {enemy.name} avec {self.weapon.name} et inflige {damage} dégâts!")
                
        # Application des dégâts
        if enemy.armor and enemy.armor.defense > 0:
            enemy.armor.defense -= damage
            if enemy.armor.defense < 0:
                enemy.hp += enemy.armor.defense
                enemy.armor.defense = 0
            print(f"Il reste {enemy.armor.defense} points d'armure à {enemy.name}")
        else:
            enemy.hp -= damage
            print(f"Il reste {max(0, enemy.hp)} HP à {enemy.name}")

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_armor(self, armor):
        self.armor = armor