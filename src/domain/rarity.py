from __future__ import annotations
import random


class Rarity(float):
    @classmethod
    def new(cls) -> Rarity:
        return cls(random.random() ** 2)

    @property
    def name(self):
        if 0.0 <= self <= 0.07:
            return "Factory New"
        elif 0.07 < self <= 0.15:
            return "Minimal Wear"
        elif 0.15 < self <= 0.38:
            return "Field Tested"
        elif 0.38 < self <= 0.45:
            return "Well Worn"
        else:
            return "Battle Scarred"

    def __repr__(self):
        return f"<Rarity {self.name} {super().__repr__(self)}>"

    def __str__(self):
        return self.name
