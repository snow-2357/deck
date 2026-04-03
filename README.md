# Deck-Builder Combat Engine

An extensible card-based combat engine where weapon choice determines the player's deck and unique defensive mechanics.

## 🏗️ Architecture Overview

- **`models/`**: Defines the core data structures.
    - `card.py`: `Card` dataclass with attributes for `damage`, `block`, `heal`, `self_damage`, and `type` (Attack, Skill, Reaction).
    - `weapon.py`: `Weapon` dataclass; loads weapon definitions and starting decks from `data/weapons.json`.
    - `passive.py`: `Passive` dataclass for persistent effects.
- **`engine/`**: The core game logic.
    - `entities.py`: Contains `Character`, `Player`, and `Enemy` classes. Handles card playing logic, health management, and stance activation.
    - `combat.py`: `CombatEngine` manages turn resolution, specifically the logic for active stances during the enemy's turn.
- **`data/`**: Configuration files.
    - `weapons.json`: The source of truth for all weapons, their descriptions, special mechanics, and full starting decks.
- **`ui/`**: User interface.
    - `cli.py`: Main game loop, input handling, and state visualization.

## ⚔️ Key Mechanics

### 🛡️ Defensive Stances (Reactions)
Playing a **Reaction** card sets the player's `active_stance` based on the weapon's `special_mechanic`. This stance is resolved during the enemy's turn:
- **Parry**: 50% chance to negate all damage and counter-attack for 10 DMG. 50% chance to take 75% damage.
- **Dodge**: 50% chance to evade all damage. 50% chance to take full damage.
- **Endure**: Guaranteed reduction; the player takes only 30% of incoming damage.

### ❤️ Health & Card Effects
- **Block**: Flat damage mitigation that resets at the start of the player's turn.
- **Heal**: Restores health up to `max_health`.
- **Self-Damage**: Deals damage to the player upon playing a card (used for high-impact cards).

## 🗃️ Current Weapons
1. **Baseball Bat**: Melee/Counter. Uses **Parry**.
2. **Gun**: Ranged/Evasion. Uses **Dodge**.
3. **Mace**: Heavy Hitter. Uses **Parry**.
4. **Brass Knuckles**: Brawler/Risk-Reward. Uses **Endure**, features high damage with self-harm and healing.

## 🛠️ Adding New Content
- **New Weapon**: Add a new entry to `data/weapons.json` with a unique ID and deck.
- **New Mechanic**: 
    1. Update `Card` model if new attributes are needed.
    2. Update `Player.play_card` in `entities.py` for play-time effects.
    3. Update `CombatEngine.resolve_enemy_turn` in `combat.py` for turn-resolution effects.
