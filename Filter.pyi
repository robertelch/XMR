import re
from typing import Callable, Optional
from bs4 import Tag


class Filter:
    """
    Represents a callable filter for XML elements (bs4.Tag),
    allowing attribute-based matching with logical combinators.

    :param func: A callable that takes a Tag and returns a bool indicating
                 whether the element matches the filter criteria.
    :type func: Optional[Callable[[Tag], bool]]
    """

    func: Callable[[Tag], bool]

    def __init__(self, func: Optional[Callable[[Tag], bool]] = None) -> None:
        """
        Initialize the Filter with a callable function.
        If no function is provided, the filter matches all elements.

        :param func: Callable filter function.
        :type func: Optional[Callable[[Tag], bool]]
        :return: None
        """
        ...

    def __call__(self, element: Tag) -> bool:
        """
        Evaluate the filter against a given Tag element.

        :param element: A BeautifulSoup Tag element to test.
        :type element: bs4.element.Tag
        :return: True if the element matches the filter criteria, False otherwise.
        :rtype: bool
        """
        ...

    @classmethod
    def contains(cls, attr_name: str, value: str) -> 'Filter':
        """
        Create a filter that matches if the specified attribute contains the given substring.

        :param attr_name: Name of the attribute to check.
        :type attr_name: str
        :param value: Substring to search for within the attribute's value.
        :type value: str
        :return: A Filter instance matching elements whose attribute contains the value.
        :rtype: Filter
        """
        ...

    @classmethod
    def not_contains(cls, attr_name: str, value: str) -> 'Filter':
        """
        Create a filter that matches if the specified attribute does NOT contain the given substring.

        :param attr_name: Name of the attribute to check.
        :type attr_name: str
        :param value: Substring that must not appear in the attribute's value.
        :type value: str
        :return: A Filter instance matching elements whose attribute does NOT contain the value.
        :rtype: Filter
        """
        ...

    @classmethod
    def equals(cls, attr_name: str, value: str) -> 'Filter':
        """
        Create a filter that matches if the specified attribute equals the given value exactly.

        :param attr_name: Name of the attribute to check.
        :type attr_name: str
        :param value: Exact string value to match.
        :type value: str
        :return: A Filter instance matching elements whose attribute equals the value.
        :rtype: Filter
        """
        ...

    @classmethod
    def not_equals(cls, attr_name: str, value: str) -> 'Filter':
        """
        Create a filter that matches if the specified attribute does NOT equal the given value.

        :param attr_name: Name of the attribute to check.
        :type attr_name: str
        :param value: Value that the attribute must not exactly match.
        :type value: str
        :return: A Filter instance matching elements whose attribute does NOT equal the value.
        :rtype: Filter
        """
        ...

    @classmethod
    def starts_with(cls, attr_name: str, value: str) -> 'Filter':
        """
        Create a filter that matches if the specified attribute's value starts with the given prefix.

        :param attr_name: Name of the attribute to check.
        :type attr_name: str
        :param value: Prefix string that the attribute value must start with.
        :type value: str
        :return: A Filter instance matching elements whose attribute starts with the value.
        :rtype: Filter
        """
        ...

    @classmethod
    def ends_with(cls, attr_name: str, value: str) -> 'Filter':
        """
        Create a filter that matches if the specified attribute's value ends with the given suffix.

        :param attr_name: Name of the attribute to check.
        :type attr_name: str
        :param value: Suffix string that the attribute value must end with.
        :type value: str
        :return: A Filter instance matching elements whose attribute ends with the value.
        :rtype: Filter
        """
        ...

    @classmethod
    def matches(cls, attr_name: str, pattern: str) -> 'Filter':
        """
        Create a filter that matches if the specified attribute's value matches the given regex pattern.

        :param attr_name: Name of the attribute to check.
        :type attr_name: str
        :param pattern: Regular expression pattern string to match.
        :type pattern: str
        :return: A Filter instance matching elements whose attribute matches the regex pattern.
        :rtype: Filter
        """
        ...

    @classmethod
    def exists(cls, attr_name: str) -> 'Filter':
        """
        Create a filter that matches if the specified attribute exists on the element.

        :param attr_name: Name of the attribute to check for existence.
        :type attr_name: str
        :return: A Filter instance matching elements having the specified attribute.
        :rtype: Filter
        """
        ...

    @classmethod
    def not_exists(cls, attr_name: str) -> 'Filter':
        """
        Create a filter that matches if the specified attribute does NOT exist on the element.

        :param attr_name: Name of the attribute to check absence.
        :type attr_name: str
        :return: A Filter instance matching elements lacking the specified attribute.
        :rtype: Filter
        """
        ...

    def __and__(self, other: 'Filter') -> 'Filter':
        """
        Combine two filters with logical AND operation.

        :param other: Another Filter instance to combine.
        :type other: Filter
        :return: A Filter instance matching elements that satisfy both filters.
        :rtype: Filter
        """
        ...

    def __or__(self, other: 'Filter') -> 'Filter':
        """
        Combine two filters with logical OR operation.

        :param other: Another Filter instance to combine.
        :type other: Filter
        :return: A Filter instance matching elements that satisfy at least one filter.
        :rtype: Filter
        """
        ...

    def __invert__(self) -> 'Filter':
        """
        Negate the filter, matching elements that do NOT satisfy this filter.

        :return: A Filter instance matching elements failing this filter.
        :rtype: Filter
        """
        ...

    def and_(self, other: 'Filter') -> 'Filter':
        """
        Fluent method to combine two filters with logical AND.

        :param other: Another Filter instance.
        :type other: Filter
        :return: A Filter instance matching elements passing both filters.
        :rtype: Filter
        """
        ...

    def or_(self, other: 'Filter') -> 'Filter':
        """
        Fluent method to combine two filters with logical OR.

        :param other: Another Filter instance.
        :type other: Filter
        :return: A Filter instance matching elements passing either filter.
        :rtype: Filter
        """
        ...

    def invert(self) -> 'Filter':
        """
        Fluent method to negate the filter.

        :return: A Filter instance matching elements not passing this filter.
        :rtype: Filter
        """
        ...
