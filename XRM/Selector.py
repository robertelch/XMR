from typing import Callable
from XRM import Filter, StringList
from bs4 import BeautifulSoup, Tag, NavigableString


class Selector:
    def __init__(self, elements: Tag | list[Tag] | 'Selector'):
        if isinstance(elements, Selector):
            elements = elements.elements
        elif isinstance(elements, list):
            elements = [el if isinstance(el, Tag) else el.element for el in elements]
        else:
            elements = [elements]
        seen = set()
        result = []
        for item in elements:
            if id(item) not in seen:
                seen.add(id(item))
                result.append(item)
        self.elements: list[Tag] = result

    def __repr__(self):
        names = [el.name for el in self.elements]
        return f"Selector([{', '.join(names)}])"

    def __iter__(self):
        for el in self.elements:
            yield Selector(el)

    def __eq__(self, other: 'Selector'):
        if not isinstance(other, Selector):
            return NotImplemented
        return self.elements == other.elements

    def __ne__(self, other: 'Selector'):
        if not isinstance(other, Selector):
            return NotImplemented
        return self.elements != other.elements  

    def __add__(self, other: 'Selector'):
        if not isinstance(other, Selector):
            return NotImplemented
        return Selector(self.elements + other.elements)
    
    def __reversed__(self):
        return Selector(list(reversed(self.elements)))
    
    def __str__(self):
        return f"<Selector with {len(self.elements)} elements>"

    def __bool__(self):
        return bool(self.elements)

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, index) -> 'Selector':
        try:
            return Selector(self.elements[index])
        except IndexError:
            return Selector([])

    @classmethod
    def from_html_string(cls, htmlstr: str) -> 'Selector':
        soup = BeautifulSoup(htmlstr, "lxml")
        return cls(soup)
    
    def __wildcard_check(self, tag: str):
        return True if tag == "*" else tag
    
    def __collect_truthy(self, func: Callable[[Tag], Tag | list[Tag]]) -> list[Tag]:
        result = []
        for el in self.elements:
            val = func(el)
            if val:
                if isinstance(val, Tag):
                    result.append(val)
                elif isinstance(val, list):
                    result.extend(val)
        return result

    def text(self) -> StringList:
        text = [t for e in self.elements if (t := e.get_text(strip=True))]
        return StringList(text)

    def preceding_siblings(self, tag: str = "*") -> 'Selector':
        tag = self.__wildcard_check(tag)
        siblings = self.__collect_truthy(lambda el: el.find_previous_siblings(tag))
        return Selector(siblings)

    def following_siblings(self, tag: str = "*") -> 'Selector':
        tag = self.__wildcard_check(tag)
        siblings = self.__collect_truthy(lambda el: el.find_next_siblings(tag))
        return Selector(siblings)

    def siblings(self, tag: str = "*"):
        tag = self.__wildcard_check(tag)
        siblings = self.preceding_siblings(tag) + self.following_siblings(tag) 
        return siblings

    def descendants(self, tag: str = "*") -> 'Selector':
        tag = self.__wildcard_check(tag)
        siblings = self.__collect_truthy(lambda el: el.find_all(tag))
        return Selector(siblings)

    def parent(self) -> 'Selector':
        found = self.__collect_truthy(lambda el: el.parent)
        return Selector(found)

    def children(self, tag: str = "*") -> 'Selector':
        tag = self.__wildcard_check(tag)
        found = self.__collect_truthy(lambda el: el.find_all(tag, recursive=False))
        return Selector(found)

    def __nth_sub_element(self, tag: str = "*", n: int = 1, recursive: bool = True) -> 'Selector':
        tag = self.__wildcard_check(tag)
        found = [match[n - 1] for el in self.elements if (match := el.find_all(tag, recursive=recursive)) and len(match) >= n]
        return Selector(found)

    def nth_descendant(self, tag: str = "*", n: int = 1) -> 'Selector':
        return self.__nth_sub_element(tag, n, recursive=True)
        
    def nth_child(self, tag: str = "*", n: int = 1) -> 'Selector':
        return self.__nth_sub_element(tag, n, recursive=False)

    def get_attribute(self, attribute: str) -> StringList:
        return StringList([el.get(attribute) for el in self.elements])

    def filter(self, filter_obj: Filter) -> 'Selector':
        filtered_elements = [el for el in self.elements if filter_obj(el)]
        return Selector(filtered_elements)

    def own_text(self) -> StringList:
        texts = []
        for el in self.elements:
            own_strings = [str(t).strip() for t in el.contents if isinstance(t, NavigableString)]
            combined = ' '.join(s for s in own_strings if s)
            if combined:
                texts.append(combined)
        return StringList(texts)