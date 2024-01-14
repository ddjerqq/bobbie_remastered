class Wallet(int):
    def transfer_to(self, other: "Wallet", amount: int) -> None:
        self -= amount
        other += amount
