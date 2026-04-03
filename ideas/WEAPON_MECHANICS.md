# Weapon Mechanics & Card Archetypes

## Weapon Selection
At the start of the game, the player selects their primary weapon. This choice determines their starting deck and unique reaction mechanics.

### 1. The Baseball Bat (Melee/Counter)
Focuses on reliable defense and high-risk counter-attacks.

*   **Swing (Basic):** Deals flat physical damage.
*   **Guard (Basic):** Provides a flat amount of Block/Shield.
*   **Block (Reaction):**
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

### 3. The Brass Knuckles (Brawler/Endurance)
Street fighting style. High risk, high reward with self-damage and healing.

*   **Hard Hit (Basic):** Deals high damage but also deals damage to the player.
*   **Rage (Skill):** Heal a portion of HP.
*   **Boxing Guard (Reaction):**
    *   **Cost:** 1 Energy.
    *   **Effect:** Enter an "Endure" stance.
    *   **Trigger (Enemy Turn):** Take only 30% of incoming damage (70% reduction). Unlike Parry/Dodge, it's guaranteed reduction but you still take some damage.

## Implementation Logic (Reactions)
1.  **Stance Activation:** Playing a "Parry", "Dodge", or "Endure" card sets a `active_stance` flag.
2.  **Resolution Phase:** During the `Enemy Turn`, before damage is applied, the engine checks the `active_stance`.
3.  **Random Roll (for Parry/Dodge):** If "Parry" or "Dodge" is active, the engine rolls (e.g., 50% chance).
4.  **Damage Calculation:**
    *   If **Success (Parry/Dodge)**: Damage is 0.
    *   If **Failure (Parry/Dodge)**: Damage is mitigated (0.75 for Parry, 1.0 for Dodge).
    *   If **Endure**: Damage is strictly 0.3x.
5.  **Cleanup:** Reset the stance flags at the end of the enemy turn.
