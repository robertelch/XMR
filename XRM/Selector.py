from XRM import Filter
from bs4 import BeautifulSoup, Tag
from typing import Union, List, Optional

class StringList:
    def __init__(self, elements: list[str]):
        self.elements = elements

    def split_and_index(self, split_char: str, index: int) -> 'StringList':
        return StringList([el.split(split_char)[index] for el in self.elements])
    
    def __iter__(self):
        return iter(self.elements)
    
    def __len__(self):
        return len(self.elements)

    def __repr__(self):
        return repr(self.elements)
    
    def __bool__(self):
        return bool(self.elements)
    
    def __getitem__(self, index):
        return self.elements[index]
    
    def as_list(self):
        return self.elements

class Selector:
    def __init__(self, elements: Union[Tag, List[Tag], 'Selector']):
        if isinstance(elements, Selector):
            elements = elements.elements
        elif isinstance(elements, list):
            elements = [el if isinstance(el, Tag) else el.element for el in elements]
        else:
            elements = [elements]
        seen = set()
        result = []
        for item in elements:
            if item not in seen:
                seen.add(item)
                result.append(item)
        self.elements: list[Tag] = result

    def __repr__(self):
        names = [el.name for el in self.elements]
        return f"Selector([{', '.join(names)}])"

    def __iter__(self):
        return iter(self.elements)

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
        root = soup.html if soup.html else soup
        children = [el for el in root.children if isinstance(el, Tag)]
        return cls(children)
    
    def text(self) -> StringList:
        text = []
        for element in self.elements:
            if t := element.get_text():
                text.append(t)
        return StringList(text)

    def descendants(self, tag: str) -> 'Selector':
        found = []
        for el in self.elements:
            found.extend(el.find_all(tag))
        return Selector(found)

    def parent(self) -> 'Selector':
        found = []
        for el in self.elements:
            if par := el.parent:
                found.append(par)
        return Selector(found)

    def children(self, tag: str) -> 'Selector':
        found = []
        for el in self.elements:
            found.extend(el.find_all(tag, recursive=False))
        return Selector(found)

    def nth_descendant(self, tag: str, n: int) -> 'Selector':
        found = []
        for el in self.elements:
            matches = el.find_all(tag)
            if len(matches) >= n:
                found.append(matches[n - 1])
        return Selector(found)

    def contains(self, attr: str, value: str) -> 'Selector':
        found = [el for el in self.elements if el.has_attr(attr) and value in el[attr]]
        return Selector(found)

    def get_attribute(self, attribute: str) -> StringList:
        return StringList([el.get(attribute) for el in self.elements])

    def filter(self, filter_obj: Filter) -> 'Selector':
        filtered_elements = [el for el in self.elements if filter_obj(el)]
        return Selector(filtered_elements)

