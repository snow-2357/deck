from dataclasses import dataclass
from typing import List
from .card import Card

@dataclass
class Weapon:
    name: str
    description: str
    starting_deck: List[Card]
    special_mechanic: str  # "Parry", "Dodge"
    
    def __str__(self):
        return f"{self.name}: {self.description}"

def create_starter_deck(weapon_type: str) -> List[Card]:
    deck = []
    if weapon_type == "Sword":
        # 5 Attacks, 4 Blocks, 1 Parry
        for _ in range(5):
            deck.append(Card("Slash", 1, "Attack", damage=6))
        for _ in range(4):
            deck.append(Card("Guard", 1, "Skill", block=5))
        deck.append(Card("Parry", 1, "Reaction", description="50% chance to negate damage and counter."))
    elif weapon_type == "Gun":
        # 5 Fires, 4 Hides, 1 Dodge
        for _ in range(5):
            deck.append(Card("Shoot", 1, "Attack", damage=8))
        for _ in range(4):
            deck.append(Card("Take Cover", 1, "Skill", block=3))
        deck.append(Card("Dodge", 1, "Reaction", description="50% chance to completely evade."))
    return deck

WEAPONS = {
    "1": Weapon("Sword", "High defense and counter-attacks.", create_starter_deck("Sword"), "Parry"),
    "2": Weapon("Gun", "High damage and evasion.", create_starter_deck("Gun"), "Dodge")
}
