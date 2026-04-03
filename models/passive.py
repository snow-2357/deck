from dataclasses import dataclass
from typing import Dict

@dataclass
class Passive:
    name: str
    description: str
    trigger: str  # "on_play", "on_turn_start", "on_enemy_hit", "on_damage_taken"
    effect_value: int = 0
    
    def apply(self, context: Dict):
        # Implementation of passive logic based on trigger
        pass
