import json
import os
from dataclasses import dataclass
from typing import List, Dict
from .card import Card

@dataclass
class Weapon:
    name: str
    description: str
    starting_deck: List[Card]
    special_mechanic: str  # "Parry", "Dodge"
    
    def __str__(self):
        return f"{self.name}: {self.description}"

def load_weapons_from_data() -> Dict[str, Weapon]:
    weapons = {}
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "weapons.json")
    
    try:
        with open(data_path, 'r') as f:
            weapon_data_list = json.load(f)
            
        for w_data in weapon_data_list:
            deck = []
            for c_data in w_data.get("deck", []):
                # Handle card counts (if provided)
                count = c_data.get("count", 1)
                for _ in range(count):
                    deck.append(Card(
                        name=c_data["name"],
                        cost=c_data["cost"],
                        type=c_data["type"],
                        damage=c_data.get("damage", 0),
                        block=c_data.get("block", 0),
                        description=c_data.get("description", "")
                    ))
            
            weapon = Weapon(
                name=w_data["name"],
                description=w_data["description"],
                starting_deck=deck,
                special_mechanic=w_data["special_mechanic"]
            )
            weapons[w_data["id"]] = weapon
    except FileNotFoundError:
        print(f"Warning: Weapon data file not found at {data_path}")
    except Exception as e:
        print(f"Error loading weapon data: {e}")
        
    return weapons

# Populate WEAPONS from data
WEAPONS = load_weapons_from_data()
