import random
from gear.armure import Armor
from characters.wizzard import Wizzard
from characters.barbarian import Barbarian
from gear.weapon import Weapon, Spell

# Créer les armes et sorts
axe = Weapon('Hache à 2 mains', 35)
sword = Weapon('Épée', 40)
wand = Weapon('Baguette de sureau', 25)
fire_wand = Weapon('Baguette de feu', 30)
fireball = Spell('Boule de feu', 75, 50)

def choose_character():
    print("=== CHOIX DU PERSONNAGE ===")
    print("1. Sorcière (Marie)")
    print("2. Barbare (Thor)")

    choice = input("Choisissez (1-2): ")

    if choice == "1":
        character = Wizzard('Marie', 150, None, None, 100, fireball)
        print("Vous jouez Marie la Sorcière.")
        return character
        
    if choice == "2":
        character = Barbarian('Thor', 200)
        print("Vous jouez Thor le Barbare.")
        return character
        
    print("Choix invalide!")
    return choose_character()

def choose_enemy(player):
    if isinstance(player, Wizzard):
        enemy = Barbarian('Thor (IA)', 175)
        print("Votre ennemi: Thor")
        return enemy
        
    enemy = Wizzard('Marie (IA)', 150, None, None, 100, fireball)
    print("Votre ennemi: Marie")
    return enemy

def choose_weapon_wizard():
    print("Armes pour Sorcière:")
    print("1. Baguette de sureau")
    print("2. Baguette de feu")
    choice = input("Choix (1-2): ")
    
    if choice == "1":
        return wand
        
    return fire_wand

def choose_weapon_barbarian():
    print("Armes pour Barbare:")
    print("1. Hache")
    print("2. Épée")
    choice = input("Choix (1-2): ")
    
    if choice == "1":
        return axe
        
    return sword

def choose_weapon(character):
    if isinstance(character, Wizzard):
        return choose_weapon_wizard()
        
    return choose_weapon_barbarian()

def choose_armor():
    print("Armures disponibles:")
    print("1. Fer (75 défense)")
    print("2. Diamant (100 défense)")
    print("3. Netherite (150 défense)")
    
    choice = input("Choix (1-3): ")
    
    if choice == "1":
        return Armor("Fer", 75, "Rare")
        
    if choice == "2":
        return Armor("Diamant", 100, "Épique")
        
    return Armor("Netherite", 150, "Légendaire")

def get_random_weapon_for_wizard():
    return random.choice([wand, fire_wand])

def get_random_weapon_for_barbarian():
    return random.choice([axe, sword])

def get_random_armor():
    armors = [
        Armor("Fer", 75, "Rare"),
        Armor("Diamant", 100, "Épique"),
        Armor("Netherite", 150, "Légendaire")
    ]
    return random.choice(armors)

def enemy_equipment(enemy):
    if isinstance(enemy, Wizzard):
        weapon = get_random_weapon_for_wizard()
    
    if isinstance(enemy, Barbarian):
        weapon = get_random_weapon_for_barbarian()
    
    armor = get_random_armor()
    return weapon, armor

def setup_player_equipment(player):
    player_weapon = choose_weapon(player)
    player.equip_weapon(player_weapon)
    
    player_armor = choose_armor()
    player.equip_armor(player_armor)

def setup_enemy_equipment(enemy):
    enemy_weapon, enemy_armor = enemy_equipment(enemy)
    enemy.equip_weapon(enemy_weapon)
    enemy.equip_armor(enemy_armor)

def check_victory(player, enemy):
    if enemy.hp <= 0:
        print(f"\n🎉 VICTOIRE! {enemy.name} est vaincu!")
        return True
        
    if player.hp <= 0:
        print(f"\n DÉFAITE! {player.name} est vaincu...")
        return True
        
    return False

def play_round(player, enemy, round_num):
    print(f"\n--- ROUND {round_num} ---")
    
    # Tour du joueur
    print(f"\nTour de {player.name}:")
    player.attack(enemy)
    
    if check_victory(player, enemy):
        return False
    
    # Tour de l'ennemi
    print(f"\nTour de {enemy.name}:")
    enemy.attack(player)
    
    if check_victory(player, enemy):
        return False
    
    input("\nAppuyez sur Entrée pour continuer...")
    return True

def game_loop():
    print("🗡️ BIENVENUE DANS L'ARENE ! ")
    
    # Création des personnages
    player = choose_character()
    enemy = choose_enemy(player)
    
    # Marquer le joueur
    player.is_player = True

    # Équipement
    setup_player_equipment(player)
    setup_enemy_equipment(enemy)

    # Combat
    round_num = 1
    while play_round(player, enemy, round_num):
        round_num += 1

# Lancer le jeu
if __name__ == "__main__":
    game_loop()