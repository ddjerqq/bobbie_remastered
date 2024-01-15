from __future__ import annotations

from dataclasses import dataclass
from domain import Item, Wallet


@dataclass
class User:
    id: int
    username: str
    experience: int
    wallet: Wallet
    items: list[Item]
