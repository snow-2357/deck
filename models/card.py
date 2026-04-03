from dataclasses import dataclass
from typing import Callable, Optional

@dataclass
class Card:
    name: str
    cost: int
    type: str  # "Attack", "Skill", "Power", "Reaction"
    damage: int = 0
    block: int = 0
    description: str = ""
    special_effect: Optional[Callable] = None

    def __str__(self):
        desc = f" | {self.description}" if self.description else ""
        stats = []
        if self.damage > 0: stats.append(f"DMG:{self.damage}")
        if self.block > 0: stats.append(f"BLK:{self.block}")
        stats_str = f" ({', '.join(stats)})" if stats else ""
        return f"[{self.name}] (Cost:{self.cost}){stats_str}{desc}"
