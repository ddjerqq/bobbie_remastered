import datetime
import time
import random


class Id:
    EPOCH = 107691120000
    __worker_increments = {i: 0 for i in range(32)}

    @classmethod
    def new(cls):
        id = time.time_ns() // 10_000_000
        id -= cls.EPOCH
        id <<= 5

        worker_id = random.randrange(0, 32)
        id += worker_id
        id <<= 5

        id += random.randrange(0, 32)
        id <<= 12

        id += cls.__worker_increments[worker_id] % 4096
        cls.__worker_increments[worker_id] += 1

        return id

    @classmethod
    def created_at(cls, id: int) -> datetime.datetime:
        ts = ((id >> 22) + cls.EPOCH) // 100
        return datetime.datetime.fromtimestamp(ts)
