import random

class Wizzard:
    def __init__(self, name, hp, weapon=None, armor=None, mana=100, spell=None):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
        self.mana = mana
        self.spell = spell

    def attack(self, enemy):
        # Si c'est le joueur
        if hasattr(self, 'is_player'):
            damage = self._player_attack_choice()
        
        # Si c'est une IA
        if not hasattr(self, 'is_player'):
            damage = self._ai_attack_choice()
                
        # Appliquer les dégâts
        self._apply_damage(enemy, damage)

    def _player_attack_choice(self):
        print(f"Mana: {self.mana}")
        print("1. Attaque avec l'arme")
        
        if self.mana >= self.spell.mana:
            print(f"2. Lancer {self.spell.name} (Coût: {self.spell.mana} mana)")
            choice = input("Choix (1-2): ")
            
            if choice == "2":
                return self._cast_spell()
        
        if self.mana < self.spell.mana:
            print("Pas assez de mana pour un sort.")
            
        return self._weapon_attack()

    def _ai_attack_choice(self):
        if self.mana >= self.spell.mana and random.randint(1, 2) == 2:
            return self._cast_spell()
            
        return self._weapon_attack()

    def _cast_spell(self):
        damage = self.spell.damage
        self.mana -= self.spell.mana
        print(f"{self.name} lance {self.spell.name}!")
        return damage

    def _weapon_attack(self):
        damage = self.weapon.damage
        print(f"{self.name} attaque avec {self.weapon.name}!")
        return damage

    def _apply_damage(self, enemy, damage):
        if enemy.armor and enemy.armor.defense > 0:
            self._damage_armor(enemy, damage)
            return
            
        enemy.hp -= damage
        print(f"Dégâts infligés: {damage}")
        print(f"HP de {enemy.name}: {max(0, enemy.hp)}")

    def _damage_armor(self, enemy, damage):
        enemy.armor.defense -= damage
        if enemy.armor.defense < 0:
            enemy.hp += enemy.armor.defense
            enemy.armor.defense = 0
        print(f"Armure endommagée! Restant: {enemy.armor.defense}")

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_armor(self, armor):
        self.armor = armor