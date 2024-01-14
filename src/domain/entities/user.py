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

    @property
    def db_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "experience": self.experience,
            "wallet": self.wallet,
        }

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f"<Db.User id={self.id} username={self.username}>"
