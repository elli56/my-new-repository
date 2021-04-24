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
        print(f"node: {self.data}")
    


class LinkedList:
    def __init__(self):
        self.__root = None
    
    def get_root(self):
        return self.__root

    def add_to_last_of_list(self, node):
        if not self.__root:
            self.__root = node
        else:
            marker = self.__root
            while marker:
                if not marker.get_next():
                    marker.set_next(node)
                    return
                marker = marker.get_next()
                            

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
    
    def size(self):
        count = 0
        marker = self.__root
        while marker:
            count += 1
            marker = marker.get_next()
        return count






class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def push(self, node):
        self.linkedlist.add_to_last_of_list(node)

    def pop(self): # В моем случае ошибка этот метод удаляет не из конца а из начала
        return self.linkedlist.remove_first()

    def find(self, node):
        return self.linkedlist.find(node)

    def len(self):
        return self.linkedlist.size()

    def print_all(self):
        self.linkedlist.print_list()











































