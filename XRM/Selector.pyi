from logging import Filter
from bs4 import Tag
from typing import Union, List

class StringList:
    def __init__(self, elements: list[str]):
        """
        Initialize a StringList instance.

        :param elements: A list of strings to be wrapped by this class.
        :type elements: list[str]
        """
    
    def split_and_index(self, split_char: str, index: int) -> 'StringList':
        """
        Split each string in the list by a given character and return a new StringList
        containing the element at the specified index from each split result.

        :param split_char: The character to split each string on.
        :type split_char: str
        :param index: The index of the split parts to extract.
        :type index: int
        :return: A new StringList containing the extracted parts.
        :rtype: StringList
        """
    
    def __iter__(self):
        """
        Return an iterator over the elements.

        :return: An iterator over the string elements.
        :rtype: iterator
        """
    
    def __len__(self):
        """
        Return the number of elements.

        :return: The number of strings in the list.
        :rtype: int
        """

    def __repr__(self):
        """
        Return a string representation of the StringList.

        :return: String representation of the wrapped list.
        :rtype: str
        """
    
    def __bool__(self):
        """
        Return True if the list has any elements, False otherwise.

        :return: True if not empty, False if empty.
        :rtype: bool
        """
    
    def __getitem__(self, index):
        """
        Return the element at the given index.

        :param index: The index to retrieve.
        :type index: int
        :return: The string at the given index.
        :rtype: str
        """

class Selector:
    def __init__(self, elements: Union[Tag, List[Tag], 'Selector']):
        """
        Initialize a Selector instance wrapping one or more BeautifulSoup Tag elements.

        :param elements: A single Tag, a list of Tags, or another Selector.
        :type elements: Union[Tag, List[Tag], Selector]
        """

    def __repr__(self):
        """
        Return a string representation of the Selector.

        :return: A representation listing the tag names of the wrapped elements.
        :rtype: str
        """

    def __iter__(self):
        """
        Return an iterator over the wrapped Tag elements.

        :return: Iterator over the elements.
        :rtype: iterator
        """

    def __bool__(self):
        """
        Return True if there are any wrapped elements, False otherwise.

        :return: True if non-empty, False if empty.
        :rtype: bool
        """

    def __getitem__(self, index) -> 'Selector':
        """
        Return a Selector wrapping the element(s) at the given index or slice.

        :param index: Index or slice of elements.
        :type index: int or slice
        :return: A new Selector containing the selected element(s).
                 If index is out of range, returns an empty Selector.
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

    def text(self) -> 'StringList':
        """
        Get the text contents of all selected Tags.

        :return: StringList of all the text contents
        :rtype: StringList
        """


    def descendants(self, tag: str) -> 'Selector':
        """
        Find all descendant elements with the given tag name.

        :param tag: The tag name to search for among descendants.
        :type tag: str
        :return: Selector wrapping all matching descendant elements.
        :rtype: Selector
        """

    def parent(self) -> 'Selector':
        """
        Get the parent elements of all wrapped elements.

        :return: Selector wrapping the parents of the current elements.
        :rtype: Selector
        """

    def children(self, tag: str) -> 'Selector':
        """
        Find all immediate children with the given tag name.

        :param tag: The tag name to search for among immediate children.
        :type tag: str
        :return: Selector wrapping all matching child elements.
        :rtype: Selector
        """

    def nth_descendant(self, tag: str, n: int) -> 'Selector':
        """
        Get the nth descendant element with the given tag from each wrapped element.

        :param tag: Tag name to search for.
        :type tag: str
        :param n: 1-based index of the descendant to select.
        :type n: int
        :return: Selector wrapping the nth matching descendant elements.
        :rtype: Selector
        """

    def contains(self, attr: str, value: str) -> 'Selector':
        """
        Select elements that have an attribute containing the given value.

        :param attr: Attribute name.
        :type attr: str
        :param value: Substring to look for inside the attribute value.
        :type value: str
        :return: Selector wrapping elements where attr contains value.
        :rtype: Selector
        """

    def get_attribute(self, attribute: str) -> StringList:
        """
        Extract the given attribute from all wrapped elements.

        :param attribute: The attribute name to extract.
        :type attribute: str
        :return: A StringList containing the attribute values.
        :rtype: StringList
        """

    def filter(self, filter_obj: Filter) -> 'Selector':
        """
        Filter elements based on a provided callable filter object.

        :param filter_obj: A callable that accepts a Tag and returns True or False.
        :type filter_obj: Filter
        :return: Selector wrapping elements for which filter_obj returns True.
        :rtype: Selector
        """
