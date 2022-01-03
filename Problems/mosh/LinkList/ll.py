class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def append_to_linked_list(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def prepend(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        list_string = ''
        while itr:
            list_string += str(itr.data) + '-->'
            itr = itr.next
        print(list_string)


if __name__ == "__main__":
    ll = LinkedList()
    ll.prepend(22)
    ll.prepend(11)
    ll.print_list()
    ll.append_to_linked_list(99)
    ll.print_list()
