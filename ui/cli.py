import os
from models.weapon import WEAPONS
from models.passive import Passive
from engine.entities import Player, Enemy
from engine.combat import CombatEngine

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_status(player, enemy, engine):
    print(f"\n--- TURN {engine.turn_count} ---")
    print(f"PLAYER: {player.health}/{player.max_health} HP | {player.block} BLK | {player.energy}/{player.max_energy} ENERGY")
    if player.active_stance:
        print(f"STANCE: {player.active_stance}")
    print(f"ENEMY: {enemy.name} | {enemy.health}/{enemy.max_health} HP | Intent: {enemy.get_intent()}")
    print("-" * 30)
    print("HAND:")
    for i, card in enumerate(player.hand):
        print(f"{i}: {card}")
    print("-" * 30)

def run_game():
    clear_screen()
    print("=== DECK-BUILDER ROGUELIKE (CLI) ===")
    print("Select your weapon:")
    for key, weapon in WEAPONS.items():
        print(f"{key}: {weapon}")
    
    choice = input("\nChoice: ")
    weapon = WEAPONS.get(choice, WEAPONS["1"])
    
    player = Player("Hero", 50, weapon)
    enemy = Enemy("Slime", 30, 8)
    engine = CombatEngine(player, enemy)
    
    # Add a starting passive for testing
    if choice == "1":
        player.passives.append(Passive("Iron Grip", "+1 Damage to all attacks", "on_play", 1))

    while player.is_alive() and enemy.is_alive():
        player.start_turn()
        
        turn_active = True
        while turn_active and enemy.is_alive():
            clear_screen()
            print_status(player, enemy, engine)
            print("Commands: [0-9] play card, 'e' end turn, 'q' quit")
            cmd = input("> ").lower()
            
            if cmd == 'e':
                turn_active = False
            elif cmd == 'q':
                return
            elif cmd.isdigit():
                idx = int(cmd)
                if not player.play_card(idx, enemy):
                    print("Invalid card or not enough energy!")
                    input("Press Enter...")
            
        if enemy.is_alive():
            print("\n--- ENEMY TURN ---")
            logs = engine.resolve_enemy_turn()
            for log in logs:
                print(log)
            engine.turn_count += 1
            input("\nPress Enter to start next turn...")
            player.end_turn()

    clear_screen()
    if player.is_alive():
        print("VICTORY! You defeated the enemy.")
    else:
        print("GAME OVER... You were defeated.")
