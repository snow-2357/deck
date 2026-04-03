import random
from .entities import Player, Enemy

class CombatEngine:
    def __init__(self, player: Player, enemy: Enemy):
        self.player = player
        self.enemy = enemy
        self.turn_count = 1

    def resolve_enemy_turn(self):
        damage = self.enemy.damage
        log = []
        
        if self.player.active_stance:
            roll = random.random()
            if self.player.active_stance == "Parry":
                if roll < 0.5:
                    log.append(f"CRITICAL PARRY! {self.player.name} negated all damage and counters for 10!")
                    self.enemy.take_damage(10)
                    damage = 0
                else:
                    log.append(f"Parry failed! {self.player.name} takes 75% damage.")
                    damage = int(damage * 0.75)
            elif self.player.active_stance == "Dodge":
                if roll < 0.5:
                    log.append(f"Evasion Success! {self.player.name} dodged the attack.")
                    damage = 0
                else:
                    log.append(f"Dodge failed! {self.player.name} takes full damage.")
            elif self.player.active_stance == "Endure":
                log.append(f"Enduring! {self.player.name} takes only 30% damage.")
                damage = int(damage * 0.3)
        
        actual_damage = self.player.take_damage(damage)
        log.append(f"{self.enemy.name} attacks for {damage} (Blocked: {damage - actual_damage})")
        return log
