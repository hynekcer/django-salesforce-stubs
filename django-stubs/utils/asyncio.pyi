from django.core.exceptions import SynchronousOnlyOperation as SynchronousOnlyOperation
from typing import TypeVar, Callable, overload

F = TypeVar('F', bound=Callable)
F2 = TypeVar('F2', bound=Callable)

@overload
def async_unsafe(message: F) -> F: ...
@overload
def async_unsafe(message: str) -> Callable[[F2], F2]: ...
