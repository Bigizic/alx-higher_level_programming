#!/usr/bin/python3
"""Singly Linked Lists module.
this module contains  a class Node that defines a node of a singly
linked list by:
SinglyLinkedList and Node objects
"""


class Node():
    """Class Node"""

    def __init__(self, data, next_node=None):
        """Constructor
        Args:
            data (int): the value of the node
            next_node (Node): the next Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter"""
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """next_node Getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node Setter"""
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """Singlylinkedlist Class"""

    def __init__(self):
        """Constructor"""
        self.__head = None

    def __str__(self):
        """print behaviour using return"""
        sll_str = ""
        node = self.__head

        if node is not None:
            while node is not None:
                sll_str += str(node.data) + '\n'
                node = node.next_node

        """Return elements in increasing order"""
        return sll_str[:-1]

    def sorted_insert(self, value):
        node = self.__head

        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)
