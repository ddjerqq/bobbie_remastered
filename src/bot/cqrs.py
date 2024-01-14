import asyncio
import time
from typing import TypeVar

from mediatr import Mediator, GenericQuery

T = TypeVar("T")


class BaseQuery(GenericQuery[T]):
    elapsed: float


class GetArrayQuery(BaseQuery[list[int]]):
    def __init__(self, items_count: int):
        self.items_count = items_count


@Mediator.behavior
async def timer_behaviour(request: BaseQuery, _next):
    request.elapsed = time.time()
    result = await _next()
    request.elapsed = f"{time.time() - request.elapsed:.6f}ms"
    return result


@Mediator.handler
class GetArrayQueryHandler:
    def handle(self, request: GetArrayQuery):
        return [i ** 2 for i in range(request.items_count)]


async def main():
    mediator = Mediator()
    request = GetArrayQuery(10)
    result = await mediator.send_async(request)
    print(result)
    print(request.elapsed)


asyncio.run(main())
