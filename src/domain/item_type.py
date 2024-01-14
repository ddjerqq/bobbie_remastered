from dataclasses import dataclass


@dataclass
class ItemType:
    id: str
    name: str
    emoji: str
    thumbnail: str | None
    price: int
    buyable: bool
