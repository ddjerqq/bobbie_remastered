class Wallet:
    __value: int

    def __init__(self, value: int):
        self.__value = value

    def try_transfer_to(self, other: "Wallet", amount: int) -> bool:
        if self.__value < amount:
            return False

        self.__value -= amount
        other.__value += amount

        return True

    @property
    def value(self):
        return self.__value

    def __repr__(self):
        return repr(self.__value)
