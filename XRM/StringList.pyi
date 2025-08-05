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
