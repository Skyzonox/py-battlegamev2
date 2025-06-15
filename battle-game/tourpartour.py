import random
from gear.armure import Armor
from characters.wizzard import Wizzard
from characters.barbarian import Barbarian
from gear.weapon import Weapon, Magic, Spell
from characters.enemy import Orc

axe = Weapon('Hacha a 2 main', 30)
wand = Magic('La baguette de sureau', 100, 10, 0.01)
sword = Weapon('Epée', 20)
wandfire = Magic('Baguette de feu', 100, 15, 0.01)
Fireboll = Spell('Boule de feu', 75, 50)

def choose_character():
    print("Choisissez votre personnage:")
    print("1. Sorcière (Marie)")
    print("2. Barbare (Thor)")

    choice = input("Choisissez votre personnage (1-2) : ")

    if choice == "1":
        character = Wizzard('Marie', 150, None, None, 100, 1, Fireboll)
        print("Vous avez choisi Marie la Sorcière.")
        return character

    elif choice == "2":
        character = Barbarian('Thor', 200, None, None)
        print("Vous avez choisi Thor le Barbare.")
        return character

    else:
        print("Choix invalide, veuillez réessayer.")
        return choose_character()

def choose_enemy(player_character):
    if isinstance(player_character, Wizzard):
        enemy = Barbarian('Thor', 175, None, None)
        print("Vous allez combattre Thor.")
    else:
        enemy = Wizzard('Marie', 150, None, None, 100, 1, Fireboll)
        print("Vous allez combattre Marie.")
    return enemy

def choose_weapon(character):
    axe = Weapon('Hacha a 2 main', 35)
    wand = Magic('La baguette de sureau', 25, 10, 0.01)
    wandfire = Magic('Baguette de feu', 30, 15, 0.01)
    sword = Weapon('Epée', 40)

    if isinstance(character, Wizzard):
        print("Armes disponibles pour Sorcière :")
        print("1. Baguette de sureau")
        print("2. Baguette de feu")
        choice = input("Choisissez votre arme (1-2) : ")
        
        if choice == "1":
            print("Vous avez choisi Baguette de sureau.")
            return wand
        elif choice == "2":
            print("Vous avez choisi Baguette de feu.")
            return wandfire
        else:
            print("Choix invalide.")
            return choose_weapon(character)

    elif isinstance(character, Barbarian):
        print("Armes disponibles pour Barbare :")
        print("1. Hache")
        print("2. Épée")
        choice = input("Choisissez votre arme (1-2) : ")
        
        if choice == "1":
            print("Vous avez choisi Hache.")
            return axe
        elif choice == "2":
            print("Vous avez choisi Épée.")
            return sword
        else:
            print("Choix invalide.")
            return choose_weapon(character)

def choose_armor():
    print("Choisissez une armure :")
    print("1. Fer (75)")
    print("2. Diamant (100)")
    print("3. Netherite (150)")
    
    choice = input("Choisissez votre armure (1-3) : ")
    
    Iron = Armor("Fer", 75, "Rare")
    Diamond = Armor("Diamant", 100, "Épique")
    Netherite = Armor("Netherite", 150, "Légendaire")
    
    if choice == "1":
        print("Vous avez choisi l'armure Fer.")
        return Iron
    elif choice == "2":
        print("Vous avez choisi l'armure Diamant.")
        return Diamond
    elif choice == "3":
        print("Vous avez choisi l'armure Netherite.")
        return Netherite
    else:
        print("Choix invalide.")
        return choose_armor()

def enemy_weapon(enemy):
    axe = Weapon("Hacha a 2 main", 30)
    sword = Weapon("Épée", 20)
    wand = Magic("La baguette de sureau", 25, 10, 0.01)
    wandfire = Magic("Baguette de feu", 30, 15, 0.01)

    if isinstance(enemy, Wizzard):
        return random.choice([wand, wandfire])
    elif isinstance(enemy, Barbarian):
        return random.choice([axe, sword])

def attack(attacker, defender):
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
                    print(f"Thor reçoit {damage} dégâts avec le sort {attacker.spell.name}.")
                    print(f"Sort utilisé : {attacker.spell.name} inflige {damage} dégâts. Mana restant : {attacker.mana}.")
                else:
                    print("Mana insuffisant! Attaque normale effectuée.")
                    damage = attacker.weapon.damage
                    attacker.weapon.attack(defender)
                    print(f"Thor reçoit {damage} dégâts avec l'arme {attacker.weapon.name}.")
            else:
                damage = attacker.weapon.damage
                attacker.weapon.attack(defender)
                print(f"Thor reçoit {damage} dégâts avec l'arme {attacker.weapon.name}.")
        else:
            print("Mana épuisé! Attaque normale est utilisée automatiquement.")
            damage = attacker.weapon.damage
            attacker.weapon.attack(defender)
            print(f"Thor reçoit {damage} dégâts avec l'arme {attacker.weapon.name}.")
    elif isinstance(attacker, Barbarian):
        damage = attacker.weapon.damage
        attacker.weapon.attack(defender)
        print(f"Barbare attaque normalement et inflige {damage} dégâts.")
    
    print(f"Points de vie restants pour {defender.name}: {max(defender.hp, 0)} PV.\n")

def game_loop():
    print("=== BIENVENUE DANS LE JEU DE COMBAT ===")
    
    player = choose_character()
    enemy = choose_enemy(player)
    
    # Ajouter un attribut pour identifier le joueur
    player.is_player = True

    player_weapon = choose_weapon(player)
    player.equip_weapon(player_weapon)
    
    enemy_weapon_choice = enemy_weapon(enemy)
    enemy.equip_weapon(enemy_weapon_choice)
    
    player_armor = choose_armor()
    player.equip_armor(player_armor)
    
    enemy_armor_choice = Armor("Diamant", 100, "Épique")
    enemy.equip_armor(enemy_armor_choice)

    round_count = 1
    while player.hp > 0 and enemy.hp > 0:
        print(f"\n--- Round {round_count} ---")
        
        # Tour du joueur
        print(f"\nC'est à {player.name} de jouer!")
        player.attack(enemy)
        if enemy.hp <= 0:
            print(f"Victoire! Vous avez vaincu {enemy.name}!")
            break
        
        # Tour de l'ennemi
        print(f"\nC'est à {enemy.name} de jouer!")
        enemy.attack(player)
        if player.hp <= 0:
            print(f"Défaite... {enemy.name} vous a vaincu.")
            break
        
        round_count += 1

game_loop()
