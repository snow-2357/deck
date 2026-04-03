# Weapon Mechanics & Card Archetypes

## Weapon Selection
At the start of the game, the player selects their primary weapon. This choice determines their starting deck and unique reaction mechanics.

### 1. The Sword (Melee/Counter)
Focuses on reliable defense and high-risk counter-attacks.

*   **Attack (Basic):** Deals flat physical damage.
*   **Defence (Basic):** Provides a flat amount of Block/Shield.
*   **Parry (Reaction):**
    *   **Cost:** 1 Energy (or free, depending on balance).
    *   **Effect:** Playable with no immediate effect. It prepares the player for a "Parry" attempt on the enemy's next attack.
    *   **Trigger (Enemy Turn):** 
        *   **Success (e.g., 50% chance):** Negate all incoming damage and deal significant counter-damage to the attacker.
        *   **Failure (e.g., 50% chance):** The player takes 70% - 80% of the incoming damage (partial mitigation).

### 2. The Gun (Ranged/Evasion)
Focuses on outputting damage while utilizing stealth and agility to avoid hits.

*   **Fire (Basic):** Deals flat ranged damage.
*   **Hide (Basic):** Provides a flat amount of Block (flavored as finding cover).
*   **Dodge (Reaction):**
    *   **Cost:** 1 Energy.
    *   **Effect:** Playable with no immediate effect. Prepares a "Dodge" or "Bullet Stop" stance.
    *   **Trigger (Enemy Turn):**
        *   **Success:** Complete evasion of the attack (Bullet Stop).
        *   **Failure:** Player takes full damage (or minimal mitigation).

## Implementation Logic (Reactions)
1.  **Stance Activation:** Playing a "Parry" or "Dodge" card sets a `weapon_stance` flag on the Player object (e.g., `is_parrying = True`).
2.  **Resolution Phase:** During the `Enemy Turn`, before damage is applied, the engine checks the `weapon_stance` flag.
3.  **Random Roll:** If a stance is active, the engine rolls a percentage (e.g., `random.random() < 0.5`).
4.  **Damage Calculation:**
    *   If **Success**: Damage is set to 0, and counter-effects are applied.
    *   If **Failure**: Damage is multiplied by the penalty (0.8 for Parry, 1.0 for Dodge).
5.  **Cleanup:** Reset the stance flags at the end of the enemy turn.
