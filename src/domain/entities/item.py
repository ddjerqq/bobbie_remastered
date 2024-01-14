from __future__ import annotations

from datetime import datetime

from domain.id import Id
from domain import ItemType, Rarity


class Item:
    id: int
    type: ItemType
    rarity: Rarity
    owner_id: int | None

    @property
    def name(self) -> str:
        return self.type.name

    @property
    def price(self) -> int:
        p = self.type.price + 1 / self.rarity
        return round(p)

    @property
    def buyable(self):
        return self.type.buyable

    @property
    def emoji(self) -> str:
        return self.type.emoji

    @property
    def thumbnail(self) -> str | None:
        return self.type.thumbnail

    @property
    def created_at(self) -> datetime:
        return Id.created_at(self.id)

    def __repr__(self):
        return f"<Item id={self.id} type={self.type!r} owner={self.owner_id} rarity={self.rarity!r}>"
