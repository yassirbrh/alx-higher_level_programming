#!/usr/bin/python3

""" Declaration of the class Node """


class Node:

    """ Initialisation of the class Node """

    __data = None
    __next_node = None

    def __init__(self, data, next_node=None):

        """ Initialisation of the constructor of the Node class """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):

        """ Initialisation of the function getter data """
        return self.__data

    @data.setter
    def data(self, value):

        """ Initialisation of the function setter data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):

        """ Initialisation of the function getter next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):

        """ Initialisation of the function setter next_node """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" Declaration of the class SinglyLinkedList """


class SinglyLinkedList:

    """ Initialisation of the class SinglyLinkedList """

    __head = None

    def __init__(self):

        """ Initialisation of the constructor of the class SinglyLinkedList """

        self.__head = None

    def sorted_insert(self, value):

        """ Creation of the function sorted_insert to insert data increasly """

        if self.__head is None:
            self.__head = Node(value)
        else:
            node = self.__head
            new_node = Node(value)
            added = False
            if node.data > new_node.data:
                self.__head = new_node
                new_node.next_node = node
                added = True
            while node.next_node and not added:
                if node.next_node.data > new_node.data:
                    new_node.next_node = node.next_node
                    node.next_node = new_node
                    node = node.next_node
                    added = True
                node = node.next_node
            if not added:
                node.next_node = new_node

    def __str__(self):

        """ Function to make the object printable """

        node = self.__head
        linkedlist = []
        while node:
            linkedlist.append(str(node.data))
            node = node.next_node
        return '\n'.join(linkedlist)
