"""Module represents Doubly linked list """


class DoubleNode:
    """Class represents node of doubly linked list"""
    def __init__(self, data):
        """Constructor"""
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Class represents doubly linked list"""
    def __init__(self):
        """Constructor"""
        self.head = None
        self.tail = None

    def prepend(self, val):
        """Adds element at start"""
        new_node = DoubleNode(val)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

    def append(self, val):
        """Adds element at the end"""
        new_node = DoubleNode(val)
        new_node.prev = self.tail
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node

    def peek_front(self):
        """:return first  element of list"""
        if self.head is None:
            raise Exception('List is empty')
        else:
            return self.head.data

    def peek_back(self):
        """:return last element of list"""
        if self.tail is None:
            raise Exception('List is empty')
        else:
            return self.tail.data

    def pop_front(self):
        """deletes first element and returns it"""
        if self.head is None:
            raise Exception("Cant delete from empty list")
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            return temp.data

    def pop_back(self):
        """deletes the last element and returns it"""
        if self.tail is None:
            raise Exception("Cant delete from empty list")
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            return temp.data

    def insert_after(self, temp_node, new_data):
        """insert element after some node"""
        if temp_node is None:
            raise Exception("Given node is empty")
        if temp_node is not None:
            new_node = DoubleNode(new_data)
            new_node.next = temp_node.next
            temp_node.next = new_node
            new_node.prev = temp_node
            if new_node.next is not None:
                new_node.next.prev = new_node
            if temp_node is self.tail:
                self.tail = new_node

    def insert_before(self, temp_node, new_data):
        """insert element before some node"""
        if temp_node is None:
            raise Exception("Given node is empty")
        if temp_node is not None:
            new_node = DoubleNode(new_data)
            new_node.prev = temp_node.prev
            temp_node.prev = new_node
            new_node.next = temp_node
            if new_node.prev is not None:
                new_node.prev.next = new_node
            if temp_node is self.head:
                self.head = new_node

    def insert_at_index(self, data, index):
        """insert value at desired index"""
        new_node = DoubleNode(data)
        if index < 1:
            raise IndexError("Index out of bounds")
        elif index == 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            temp = self.head
            for i in range(1, index-1):
                if temp is not None:
                    temp = temp.next
            if temp is not None:
                new_node.next = temp.next
                new_node.prev = temp
                temp.next = new_node
                if new_node.next is not None:
                    new_node.next.prev = new_node
            else:
                print("The previous node if null")

    def print_list(self):
        """prints linked list"""
        if self.head is None:
            print("List is empty")
        start = self.head
        while start is not None:
            print(f"->{start.data}")
            start = start.next

    def look_up(self, val):
        """return index of desired element"""
        index = 0
        if self.head is None:
            print("List is empty")
        start = self.head
        while start is not None:
            if start.data == val:
                return index
            start = start.next
            index += 1
        return "No such element"

    def get_size(self):
        """:return size of list"""
        count = 0
        if self.head is None:
            return 0
        start = self.head
        while start is not None:
            start = start.next
            count += 1
        return count

    def remove_by_value(self, x):
        """remove element from list by value"""
        if self.head is None:
            raise Exception("List is empty")
        if self.head.next is None:
            if self.head.data == x:
                self.head = None
            else:
                return "Item not found"
        if self.head.data == x:
            self.head = self.head.next
            self.head.prev = None
        n = self.head
        while n.next is not None:
            if n.data == x:
                break
            n = n.next
        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            if n.data == x:
                n.prev.next = None
            else:
                return "Element not found"

    def remove_by_index(self, index):
        """remove element by index from list"""
        if self.head is None:
            raise ValueError("Deleting from empty list")
        if index < 0 or index >= self.get_size():
            raise IndexError("Index out of bounds")
        current = self.head
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            for i in range(index-1):
                current = current.next
            p = current.next.next
            if p is None:
                current.next = None
            else:
                current.next = p
                p.prev = current

    def is_empty(self):
        """:return true if list is empty"""
        return self.head is None


if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()
    print(doubly_linked_list.is_empty())
    doubly_linked_list.append(25)
    doubly_linked_list.append(11)
    doubly_linked_list.append(98)
    doubly_linked_list.append(45)
    doubly_linked_list.append(3)
    doubly_linked_list.append(126)
    doubly_linked_list.print_list()
    print('\n')
    print(doubly_linked_list.is_empty())
    doubly_linked_list.insert_at_index(24, 2)
    doubly_linked_list.remove_by_index(4)
    doubly_linked_list.print_list()
