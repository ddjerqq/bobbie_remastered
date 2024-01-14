from application.common import BaseQuery


class GetArrayQuery(BaseQuery[list[int]]):
    def __init__(self, items_count: int):
        self.items_count = items_count

