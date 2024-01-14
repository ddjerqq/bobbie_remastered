import time

from mediatr import Mediator

from application import BaseQuery


@Mediator.behavior
async def timer_behaviour(request: BaseQuery, _next):
    request.elapsed = time.time()
    result = await _next()
    request.elapsed = f"{time.time() - request.elapsed:.6f}ms"
    return result
