from lxml import etree, html
from typing import Callable, Union, List
import re
from itertools import chain

class StringList:
    def __init__(self, elements: List[str]) -> 'StringList':
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

    def __add__(self, other: Union['StringList', list]) -> 'StringList':
        if isinstance(other, StringList):
            return StringList(self.elements + other.elements)
        elif isinstance(other, list):
            return StringList(self.elements + other)
        return NotImplemented

    def split_and_index(self, split_char: str, index: int) -> 'StringList':
        return StringList([el.split(split_char)[index] for el in self.elements])

    def as_list(self) -> List[str]:
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


class Selector:
    def __init__(self, elements: Union[etree._Element, List[etree._Element], 'Selector']):
        if isinstance(elements, Selector):
            elements = elements.elements
        elif isinstance(elements, list):
            # Filter out duplicates by id
            seen = set()
            result = []
            for el in elements:
                if id(el) not in seen:
                    seen.add(id(el))
                    result.append(el)
            elements = result
        else:
            elements = [elements]
        self.elements: List[etree._Element] = elements

    def __repr__(self):
        names = [el.tag if hasattr(el, 'tag') else str(el) for el in self.elements]
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
        parser = html.HTMLParser(encoding='utf-8')
        tree = html.fromstring(htmlstr, parser=parser)
        return cls(tree)

    def __wildcard_check(self, tag: str):
        return "*" if tag == "*" else tag

    # Collect elements from function returns (which may be single element or list)
    def __collect_truthy(self, func: Callable[[etree._Element], Union[etree._Element, List[etree._Element], None]]) -> List[etree._Element]:
        result = []
        for el in self.elements:
            val = func(el)
            if val:
                if isinstance(val, list):
                    result.extend(val)
                else:
                    result.append(val)
        # Deduplicate by id
        seen = set()
        unique = []
        for el in result:
            if id(el) not in seen:
                seen.add(id(el))
                unique.append(el)
        return unique

    def text(self) -> StringList:
        texts = []
        for el in self.elements:
            text_content = ''.join(el.itertext()).strip()
            if text_content:
                texts.append(text_content)
        return StringList(texts)

    def preceding_siblings(self, tag: str = "*") -> 'Selector':
        tag = self.__wildcard_check(tag)
        def get_preceding_siblings(el):
            # lxml: get siblings before el with the same parent
            parent = el.getparent()
            if parent is None:
                return []
            siblings = []
            for sib in parent.iterchildren():
                if sib is el:
                    break
                if tag == "*" or sib.tag == tag:
                    siblings.append(sib)
            return siblings
        siblings = self.__collect_truthy(get_preceding_siblings)
        return Selector(siblings)

    def following_siblings(self, tag: str = "*") -> 'Selector':
        tag = self.__wildcard_check(tag)
        def get_following_siblings(el):
            parent = el.getparent()
            if parent is None:
                return []
            siblings = []
            found = False
            for sib in parent.iterchildren():
                if found:
                    if tag == "*" or sib.tag == tag:
                        siblings.append(sib)
                if sib is el:
                    found = True
            return siblings
        siblings = self.__collect_truthy(get_following_siblings)
        return Selector(siblings)

    def siblings(self, tag: str = "*") -> 'Selector':
        return self.preceding_siblings(tag) + self.following_siblings(tag)

    def descendants(self, tag: str = "*") -> 'Selector':
        tag = self.__wildcard_check(tag)
        descendants = []
        for el in self.elements:
            if tag == "*":
                descendants.extend(list(el.iterdescendants()))
            else:
                descendants.extend(el.iterdescendants(tag=tag))
        return Selector(descendants)

    def parent(self) -> 'Selector':
        parents = []
        for el in self.elements:
            p = el.getparent()
            if p is not None:
                parents.append(p)
        return Selector(parents)

    def children(self, tag: str = "*") -> 'Selector':
        tag = self.__wildcard_check(tag)
        children = []
        for el in self.elements:
            for child in el.iterchildren():
                if tag == "*" or child.tag == tag:
                    children.append(child)
        return Selector(children)

    def __nth_sub_element(self, tag: str = "*", n: int = 1, recursive: bool = True) -> 'Selector':
        tag = self.__wildcard_check(tag)
        found = []
        for el in self.elements:
            if recursive:
                elems = list(el.iterdescendants(tag=tag))
            else:
                elems = [c for c in el.iterchildren() if tag == "*" or c.tag == tag]
            if len(elems) >= n:
                found.append(elems[n-1])
        return Selector(found)

    def nth_descendant(self, tag: str = "*", n: int = 1) -> 'Selector':
        return self.__nth_sub_element(tag, n, recursive=True)
        
    def nth_child(self, tag: str = "*", n: int = 1) -> 'Selector':
        return self.__nth_sub_element(tag, n, recursive=False)

    def get_attribute(self, attribute: str) -> StringList:
        attrs = []
        for el in self.elements:
            val = el.get(attribute)
            attrs.append(val if val is not None else '')
        return StringList(attrs)

    # Assuming Filter is a callable that accepts an lxml Element and returns bool
    def filter(self, filter_obj: Callable[[etree._Element], bool]) -> 'Selector':
        filtered_elements = [el for el in self.elements if filter_obj(el)]
        return Selector(filtered_elements)

    def own_text(self) -> StringList:
        texts = []
        for el in self.elements:
            # Own text is text directly inside the element excluding child tags
            own_text_parts = []
            if el.text:
                own_text_parts.append(el.text.strip())
            for child in el:
                if child.tail:
                    own_text_parts.append(child.tail.strip())
            combined = ' '.join([part for part in own_text_parts if part])
            if combined:
                texts.append(combined)
        return StringList(texts)

    def xpath(self, xpath_expr: str) -> 'Selector':

        results = []
        for el in self.elements:
            res = el.xpath(xpath_expr)
            # xpath may return elements or strings, filter for elements
            if isinstance(res, list):
                for r in res:
                    if isinstance(r, etree._Element):
                        results.append(r)
                    elif isinstance(r, str):
                        # wrap text nodes in a fake element or ignore? 
                        # Here, we ignore text-only results for Selector
                        pass
            else:
                if isinstance(res, etree._Element):
                    results.append(res)
        return Selector(results)
