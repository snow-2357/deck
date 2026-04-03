# Deck-Builder Roguelike Implementation Plan (Python + Pygame)

## Objective
Create a functional deck-builder prototype with roguelike passive systems that modify card attributes and player stats.

## Architecture & Core Components

### 1. Data Models (`models.py`)
- **Card:**
  - Properties: `name`, `cost`, `damage`, `block`, `type` (Attack, Skill, Power).
  - Methods: `apply_effect(target, source)`.
- **Passive (Relic/Buff):**
  - Properties: `name`, `description`, `trigger` (on_play, on_turn_start, on_enemy_hit).
  - Effect: Modifies damage, block, energy, or card draw.

### 2. Game Logic (`engine.py`)
- **Deck Manager:**
  - `draw_pile`: Shuffled collection of cards.
  - `hand`: Cards currently playable.
  - `discard_pile`: Played or discarded cards.
- **Combat Loop:**
  1. **Player Turn Start:** Trigger passives, reset energy, draw cards.
  2. **Player Action:** Play cards (spend energy, apply effects, move to discard).
  3. **End Turn:** Discard remaining hand, trigger "end of turn" passives.
  4. **Enemy Turn:** Enemy performs action.

### 3. Roguelike Progression
- **Passive Selection:** After "battles" or at certain nodes, the player chooses from 3 randomized passives.
- **Card Modification:** Some passives or events allow increasing base damage/block of specific cards.

### 4. UI & Rendering (`gui.py`)
- **Pygame Window:** 1280x720.
- **Card Rendering:** Rectangles with text (name, cost, damage/block).
- **Hand Layout:** Horizontal alignment at the bottom.
- **Draw/Discard Piles:** Counters in the corners.
- **Player/Enemy Stats:** Health bars and status icons (passives).

## Implementation Phases

### Phase 1: MVP Core
1. Setup Pygame boilerplate.
2. Implement `Card` class and a basic `Deck`.
3. Create the `Hand` and `Piles` logic.
4. Basic rendering of cards in hand.

### Phase 2: Combat & Passives
1. Implement energy system.
2. Simple Enemy AI (static damage).
3. Passive system framework:
   - Example: "Iron Grip" (+1 damage to all Attack cards).
   - Example: "Swiftness" (Draw +1 card at turn start).

### Phase 3: Roguelike Loop
1. Post-battle reward screen (Select Passive).
2. Attribute modification (Permanent stat increases).

## Verification & Testing
- **Unit Tests:** Verify card draw/shuffle logic doesn't lose cards.
- **Manual Testing:**
  - Verify energy correctly limits card play.
  - Verify passives correctly modify card output (e.g., damage 5 becomes 6 with +1 passive).
  - Verify discard pile is reshuffled into draw pile when draw pile is empty.

## Future Considerations
- Animations (Tweening cards from deck to hand).
- Map-based progression (Slay the Spire style).
- Card upgrade system.
