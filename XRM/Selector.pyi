from typing import Callable, Union, Iterator
from bs4 import Tag
from XRM import Filter
from typing import Iterator, Union, List


class StringList:
    def __init__(self, elements: List[str]) -> 'StringList':
        """
        Initialize a StringList with a list of strings.

        :param elements: List of strings.
        :type elements: List[str]
        """

    def __iter__(self) -> Iterator[str]:
        """
        Return an iterator over the strings.

        :return: Iterator of strings.
        :rtype: Iterator[str]
        """

    def __len__(self) -> int:
        """
        Return the number of strings in the list.

        :return: Number of elements.
        :rtype: int
        """

    def __repr__(self) -> str:
        """
        Return the official string representation of the StringList.

        :return: Representation string.
        :rtype: str
        """

    def __str__(self) -> str:
        """
        Return a comma-separated string of all elements.

        :return: Concatenated string.
        :rtype: str
        """

    def __bool__(self) -> bool:
        """
        Return True if the StringList contains any elements.

        :return: True if not empty, else False.
        :rtype: bool
        """

    def __getitem__(self, index: int) -> str:
        """
        Return the string at the given index.

        :param index: Index of element.
        :return: String at index.
        :rtype: str
        """

    def __contains__(self, item: str) -> bool:
        """
        Check if a string is contained in the list.

        :param item: String to check.
        :return: True if contained, else False.
        :rtype: bool
        """

    def __add__(self, other: Union['StringList', List[str]]) -> 'StringList':
        """
        Concatenate this StringList with another StringList or list of strings.

        :param other: Another StringList or list of strings.
        :return: New concatenated StringList.
        :rtype: StringList
        """

    def split_and_index(self, split_char: str, index: int) -> 'StringList':
        """
        Split each string by split_char and select the element at the given index.

        :param split_char: Character to split by.
        :param index: Index of split part to keep.
        :return: StringList of selected parts.
        :rtype: StringList
        """

    def as_list(self) -> List[str]:
        """
        Return the underlying list of strings.

        :return: List of strings.
        :rtype: List[str]
        """

    def clean(self) -> 'StringList':
        """
        Return a new StringList with all empty strings removed.

        :return: Cleaned StringList.
        :rtype: StringList
        """

    def replace(self, old: str, new: str) -> 'StringList':
        """
        Return a new StringList where each string has old replaced by new.

        :param old: Substring to replace.
        :param new: Replacement substring.
        :return: StringList with replaced strings.
        :rtype: StringList
        """

    def strip(self) -> 'StringList':
        """
        Return a new StringList with whitespace stripped from each string.

        :return: Stripped StringList.
        :rtype: StringList
        """

    def split(self, char: str) -> 'StringList':
        """
        Split each string by the given character and flatten the result.

        :param char: Character to split by.
        :return: Flattened StringList of split parts.
        :rtype: StringList
        """

    def re_sub(self, pattern: str, repl: str) -> 'StringList':
        """
        Perform a regex substitution on each element in the list.

        :param pattern: Regex pattern to search for.
        :type pattern: str
        :param repl: Replacement string.
        :type repl: str
        :return: A new StringList with the pattern replaced by repl in each element.
        :rtype: StringList
        """

    def re_search(self, pattern: str) -> 'StringList':
        """
        Search for a regex pattern in each element and return the matched substring or None.

        :param pattern: Regex pattern to search for.
        :type pattern: str
        :return: A new StringList with the first match found in each element, or None if no match.
        :rtype: StringList
        """


class Selector:
    def __init__(self, elements: Union[Tag, list[Tag], 'Selector']) -> None:
        """
        Initialize a Selector wrapping one or multiple BeautifulSoup Tag elements.

        :param elements: A Tag, a list of Tags, or another Selector instance.
        :type elements: Tag | list[Tag] | Selector
        """

    def __repr__(self) -> str:
        """
        Return a string representation showing tag names of contained elements.

        :return: Representation string.
        :rtype: str
        """

    def __iter__(self) -> Iterator['Selector']:
        """
        Iterate over each Tag wrapped individually as a Selector.

        :return: Iterator over Selector instances each wrapping a single Tag.
        :rtype: Iterator[Selector]
        """

    def __eq__(self, other: object) -> bool:
        """
        Check equality with another Selector based on underlying elements.

        :param other: Object to compare with.
        :return: True if both have the same elements.
        :rtype: bool
        """

    def __ne__(self, other: object) -> bool:
        """
        Check inequality with another Selector based on underlying elements.

        :param other: Object to compare with.
        :return: True if elements differ.
        :rtype: bool
        """

    def __add__(self, other: 'Selector') -> 'Selector':
        """
        Combine elements of this Selector with another Selector.

        :param other: Another Selector instance.
        :return: New Selector containing elements from both.
        :rtype: Selector
        """

    def __reversed__(self) -> 'Selector':
        """
        Return a new Selector with elements in reversed order.

        :return: Reversed Selector.
        :rtype: Selector
        """

    def __str__(self) -> str:
        """
        Return a summary string for this Selector.

        :return: Summary string.
        :rtype: str
        """

    def __bool__(self) -> bool:
        """
        Return True if this Selector contains any elements.

        :return: True if elements exist, else False.
        :rtype: bool
        """

    def __len__(self) -> int:
        """
        Return the number of elements wrapped by this Selector.

        :return: Number of elements.
        :rtype: int
        """

    def __getitem__(self, index: int) -> 'Selector':
        """
        Retrieve a Selector wrapping the element(s) at the given index or slice.

        :param index: Index or slice.
        :return: Selector wrapping selected elements or empty Selector if out of range.
        :rtype: Selector
        """

    @classmethod
    def from_html_string(cls, htmlstr: str) -> 'Selector':
        """
        Create a Selector from an HTML string by parsing it and selecting the immediate children of <html>.

        :param htmlstr: A string containing HTML.
        :type htmlstr: str
        :return: Selector wrapping the immediate child elements of <html> or root if no <html> tag.
        :rtype: Selector
        """

    def text(self) -> StringList:
        """
        Extract concatenated and stripped text content of all elements.

        :return: StringList containing text from each element.
        :rtype: StringList
        """

    def preceding_siblings(self, tag: str = "*") -> 'Selector':
        """
        Get all preceding siblings matching the specified tag for each element.

        :param tag: Tag name or '*' for any tag.
        :type tag: str
        :return: Selector with preceding sibling elements.
        :rtype: Selector
        """

    def following_siblings(self, tag: str = "*") -> 'Selector':
        """
        Get all following siblings matching the specified tag for each element.

        :param tag: Tag name or '*' for any tag.
        :type tag: str
        :return: Selector with following sibling elements.
        :rtype: Selector
        """

    def siblings(self, tag: str = "*") -> 'Selector':
        """
        Get all siblings (preceding and following) matching the specified tag for each element.

        :param tag: Tag name or '*' for any tag.
        :type tag: str
        :return: Selector with all sibling elements.
        :rtype: Selector
        """

    def descendants(self, tag: str = "*") -> 'Selector':
        """
        Get all descendant elements matching the specified tag.

        :param tag: Tag name or '*' for any tag.
        :type tag: str
        :return: Selector containing all descendants.
        :rtype: Selector
        """

    def parent(self) -> 'Selector':
        """
        Get the parent elements of each element in this Selector.

        :return: Selector with parent elements.
        :rtype: Selector
        """

    def children(self, tag: str = "*") -> 'Selector':
        """
        Get direct children matching the specified tag of each element.

        :param tag: Tag name or '*' for any tag.
        :type tag: str
        :return: Selector containing children elements.
        :rtype: Selector
        """

    def nth_descendant(self, tag: str = "*", n: int = 1) -> 'Selector':
        """
        Get the nth descendant element matching the tag for each element, counting recursively.

        :param tag: Tag name or '*' for any tag.
        :param n: 1-based index of descendant.
        :return: Selector with nth descendant elements.
        :rtype: Selector
        """

    def nth_child(self, tag: str = "*", n: int = 1) -> 'Selector':
        """
        Get the nth direct child element matching the tag for each element.

        :param tag: Tag name or '*' for any tag.
        :param n: 1-based index of child.
        :return: Selector with nth child elements.
        :rtype: Selector
        """

    def get_attribute(self, attribute: str) -> StringList:
        """
        Retrieve the value of the given attribute from each element.

        :param attribute: Attribute name.
        :return: StringList of attribute values (or None where missing).
        :rtype: StringList
        """

    def filter(self, filter_obj: Filter) -> 'Selector':
        """
        Filter elements based on a callable Filter object.

        :param filter_obj: A Filter callable that takes a Tag and returns a bool.
        :return: Selector with elements that satisfy the filter.
        :rtype: Selector
        """

    def own_text(self) -> StringList:
        """
        Extract only the direct text content (not from descendants) of each element.

        :return: StringList of direct text strings for each element.
        :rtype: StringList
        """
