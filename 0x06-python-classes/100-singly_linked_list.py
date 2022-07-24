#!/usr/bin/python3
"""class module that defines a Node"""


class Node:
    """defines a Node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Constructor.
        Args:
            data(int): private instance attribute
            next_node: can be None of must be Node object
        """
        
        self.__data = data
        self.___next_node = next_node

    @property
    def data(self):
        """Raises:
            TypeError: data must be type "int
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Raise:
            TypeError: next_node must be Node object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if next_node = None or 
