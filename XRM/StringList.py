from itertools import chain
import re

class StringList:
    def __init__(self, elements: list[str]) -> 'StringList':
        self.elements = elements

    def __iter__(self):
        return iter(self.elements)
    
    def __len__(self):
        return len(self.elements)

    def __repr__(self):
        return repr(self.elements)

    def __str__(self):
        return ', '.join(self.elements)

    def __bool__(self):
        return bool(self.elements)
    
    def __getitem__(self, index) -> str:
        return self.elements[index]

    def __contains__(self, item: str):
        return item in self.elements.copy()

    def __add__(self, other: 'StringList' | list) -> 'StringList':
        if isinstance(other, StringList):
            return StringList(self.elements + other.elements)
        elif isinstance(other, list):
            return StringList(self.elements + other)
        return NotImplemented

    def __add__(self, other: 'StringList' | list) -> 'StringList':
        if isinstance(other, StringList):
            return StringList(self.elements + other.elements)
        elif isinstance(other, list):
            return StringList(self.elements + other)
        return NotImplemented

    def split_and_index(self, split_char: str, index: int) -> 'StringList':
        return StringList([el.split(split_char)[index] for el in self.elements])

    def as_list(self) -> list[str]:
        return self.elements
    
    def clean(self) -> 'StringList':
        return StringList([el for el in self.elements if el])

    def replace(self, old: str, new: str) -> 'StringList':
        return StringList([el.replace(old, new) for el in self.elements])
    
    def strip(self) -> 'StringList':
        return StringList([el.strip() for el in self.elements])

    def split(self, char: str) -> 'StringList':
        return StringList(list(chain.from_iterable([el.split(char) for el in self.elements])))
    
    def re_sub(self, pattern: str, repl: str) -> 'StringList':
        return StringList([re.sub(pattern, repl, el) for el in self.elements])
    
    def re_search(self, pattern: str) -> 'StringList':
        return StringList([(r.group() if (r := re.search(pattern, el)) else None) for el in self.elements])