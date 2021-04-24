''' queue '''

class Node:
    def __init__(self, data):
        self.data = data
        self.__next = None

    def set_next(self, node):
        if isinstance(node, Node) or node is None:
            self.__next = node
        else:
            raise TypeError("The node must be a Node child or None")
        
    def get_next(self):
        return self.__next
    
    def print_details(self):
        print f"node: {self.data}"
    


class LinkedList:
    def __init__(self):
        self.__root = None
    
    def get_root(self):
        return self.__root

    def add_to_head_list(self, node):
        if self.__root:
            self.__root.set_next(node)
        else:
            self.__root = node

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, data):
        marker = self.__root
        while marker:
            if marker.data == data:
                return marker
            marker = marker.get_next()
        raise LookupError("There are No element with such data!")

    def remove_first(self):
        if self.__root:
            head = self.__root
            self.__root = self.__root.get_next()
            return head
        raise Exception("The list is empty.")
    

class Queue:
    def __init__(self):
        self.linkedlist = LinkedList():

    def push(node):
        self.linkedlist.add_to_head_list(node)

    def pop():
        self.linkedlist.remove_first()

    def find(node):
        self.linkedlist.find(node)

    def len():
        pass












































