class Barbarian:
    def __init__(self, name, hp, weapon=None, armor=None):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor

    def attack(self, enemy):
        # Le barbare attaque deux fois
        for i in range(2):
            if enemy.hp <= 0:
                break
                
            self._single_attack(enemy)

    def _single_attack(self, enemy):
        damage = self.weapon.damage
        
        # Attaque sur l'armure si elle existe
        if enemy.armor and enemy.armor.defense > 0:
            self._attack_armor(enemy, damage)
            return
            
        # Attaque directe sur les HP
        self._attack_hp(enemy, damage)

    def _attack_armor(self, enemy, damage):
        enemy.armor.defense -= damage
        if enemy.armor.defense < 0:
            enemy.hp += enemy.armor.defense  # Les dégâts restants
            enemy.armor.defense = 0
        print(f"{self.name} attaque {enemy.name} et endommage l'armure!")
        print(f"Armure restante: {enemy.armor.defense}")

    def _attack_hp(self, enemy, damage):
        enemy.hp -= damage
        print(f"{self.name} attaque {enemy.name} et inflige {damage} dégâts!")
        print(f"HP restants: {max(0, enemy.hp)}")

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_armor(self, armor):
        self.armor = armor