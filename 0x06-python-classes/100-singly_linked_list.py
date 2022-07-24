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
        if value is None:
            if isinstance(value, Node):
                self.__next_node = value
        else:
            raise TypeError("next node must be a node")

"""
produces a linked list of sorted Node objects then print/line

"""

class SinglyLinkedList:
    """defines a singly linked list module"""
    
    def __init__(self):
        """Constructor:
        Instance:
            head: instance attribute
        """
        self.__head = head

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list"""

        def sorted_insert(self, value):
            if self.__head is None or value < self.__head.data:
                self.__head = Node(value, self.__head)
                return
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            tmp.next_node = Node(value, tmp.next_node)

    """
    Print
    """
    def __str__(self):
        if self.__head is None:
            return ("")
        tmp = self.__head
        _list = ""
        while tmp is not None:
            _list += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                _list += "\n"
        return (_list)
