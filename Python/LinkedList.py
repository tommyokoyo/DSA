class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def insert_beginning(self, data):
        """
            inserts a new node at the beginning of the list
            :param data:
            :return: No return value
        """
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def insert_at_index(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0

        if index == position:
            self.insert_beginning(data)
        else:
            while current_node is not None and position + 1 != index:
                position += 1
                current_node = current_node.next

            if current_node is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print('Index not present')

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def find(self, val):
        item = self.head

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.val)
            current_node = current_node.next


if __name__ == '__main__':
    linkedlist = LinkedList()

    linkedlist.insert_beginning('a')
    linkedlist.insert_beginning('b')
    linkedlist.insert_beginning('c')

    linkedlist.print_list()
