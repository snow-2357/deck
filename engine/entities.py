import random
from typing import List, Optional
from models.card import Card
from models.passive import Passive
from models.weapon import Weapon

class Character:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.max_health = health
        self.block = 0
        self.passives: List[Passive] = []

    def take_damage(self, amount: int):
        if self.block >= amount:
            self.block -= amount
            return 0
        else:
            damage_to_health = amount - self.block
            self.block = 0
            self.health -= damage_to_health
            return damage_to_health

    def is_alive(self):
        return self.health > 0

class Player(Character):
    def __init__(self, name: str, health: int, weapon: Weapon):
        super().__init__(name, health)
        self.weapon = weapon
        self.energy = 3
        self.max_energy = 3
        self.draw_pile = list(weapon.starting_deck)
        random.shuffle(self.draw_pile)
        self.hand: List[Card] = []
        self.discard_pile: List[Card] = []
        self.active_stance: Optional[str] = None # "Parry" or "Dodge"

    def draw_cards(self, num: int):
        for _ in range(num):
            if not self.draw_pile:
                if not self.discard_pile:
                    break
                self.draw_pile = list(self.discard_pile)
                self.discard_pile = []
                random.shuffle(self.draw_pile)
            self.hand.append(self.draw_pile.pop())

    def start_turn(self):
        self.block = 0
        self.energy = self.max_energy
        self.active_stance = None
        self.draw_cards(5)

    def play_card(self, card_idx: int, target: Character):
        if 0 <= card_idx < len(self.hand):
            card = self.hand[card_idx]
            if self.energy >= card.cost:
                self.energy -= card.cost
                
                # Apply Damage
                if card.damage > 0:
                    # Apply passives that modify damage
                    final_damage = card.damage
                    for p in self.passives:
                        if p.trigger == "on_play" and "damage" in p.name.lower():
                            final_damage += p.effect_value
                    target.take_damage(final_damage)
                
                # Apply Block
                if card.block > 0:
                    self.block += card.block
                
                # Special effects (Reactions)
                if card.type == "Reaction":
                    self.active_stance = self.weapon.special_mechanic
                
                self.discard_pile.append(self.hand.pop(card_idx))
                return True
        return False

    def end_turn(self):
        self.discard_pile.extend(self.hand)
        self.hand = []

class Enemy(Character):
    def __init__(self, name: str, health: int, damage: int):
        super().__init__(name, health)
        self.damage = damage

    def get_intent(self):
        return f"Attack for {self.damage} DMG"
