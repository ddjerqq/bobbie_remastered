from typing import TypeVar
from mediatr import GenericQuery

T = TypeVar("T")


class BaseQuery(GenericQuery[T]):
    elapsed: float
