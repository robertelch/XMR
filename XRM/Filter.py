import re
from typing import Callable, Optional, Union
from bs4 import Tag


class Filter:
    def __init__(self, func: Optional[Callable[[Tag], bool]] = None):
        self.func: Callable[[Tag], bool] = func or (lambda el: True)

    def __call__(self, element: Tag) -> bool:
        return self.func(element)

    # Factory methods
    @classmethod
    def contains(cls, attr_name: str, value: str) -> 'Filter':
        return cls(lambda el: value in (el.get(attr_name) or ''))

    @classmethod
    def not_contains(cls, attr_name: str, value: str) -> 'Filter':
        return cls(lambda el: value not in (el.get(attr_name) or ''))

    @classmethod
    def equals(cls, attr_name: str, value: str) -> 'Filter':
        return cls(lambda el: el.get(attr_name) == value)

    @classmethod
    def not_equals(cls, attr_name: str, value: str) -> 'Filter':
        return cls(lambda el: el.get(attr_name) != value)

    @classmethod
    def starts_with(cls, attr_name: str, value: str) -> 'Filter':
        return cls(lambda el: (el.get(attr_name) or '').startswith(value))

    @classmethod
    def ends_with(cls, attr_name: str, value: str) -> 'Filter':
        return cls(lambda el: (el.get(attr_name) or '').endswith(value))

    @classmethod
    def matches(cls, attr_name: str, pattern: str) -> 'Filter':
        regex = re.compile(pattern)
        return cls(lambda el: bool(regex.search(el.get(attr_name) or '')))

    @classmethod
    def exists(cls, attr_name: str) -> 'Filter':
        return cls(lambda el: el.get(attr_name) is not None)

    @classmethod
    def not_exists(cls, attr_name: str) -> 'Filter':
        return cls(lambda el: el.get(attr_name) is None)

    @classmethod
    def text_contains(cls, value: str) -> 'Filter':
        return cls(lambda el: value in (el.get_text() or ''))

    @classmethod
    def text_equals(cls, value: str) -> 'Filter':
        return cls(lambda el: (el.get_text() or '') == value)

    @classmethod
    def text_matches(cls, pattern: str) -> 'Filter':
        regex = re.compile(pattern)
        return cls(lambda el: bool(regex.search(el.get_text() or '')))

    @classmethod
    def text_exists(cls) -> 'Filter':
        return cls(lambda el: bool((el.get_text() or '').strip()))

    @classmethod
    def text_not_exists(cls) -> 'Filter':
        return cls(lambda el: not (el.get_text() or '').strip())

    # Optional fluent versions
    def and_(self, other: 'Filter') -> 'Filter':
        return self & other

    def or_(self, other: 'Filter') -> 'Filter':
        return self | other

    def invert(self) -> 'Filter':
        return ~self

    # Logical combinators
    def __and__(self, other: 'Filter') -> 'Filter':
        return Filter(lambda el: self(el) and other(el))

    def __or__(self, other: 'Filter') -> 'Filter':
        return Filter(lambda el: self(el) or other(el))

    def __invert__(self) -> 'Filter':
        return Filter(lambda el: not self(el))