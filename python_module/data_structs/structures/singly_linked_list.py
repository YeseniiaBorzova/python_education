"""Module represents Singly linked list """


class SingleNode:
    """Class represent node of singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Class represents singly linked list"""
    def __init__(self):
        """Constructor"""
        self.head = None

    def __iter__(self):
        """Iterator for doubly linked list"""
        cur = self.head
        while cur is not None:
            yield cur.data
            cur = cur.next

    def append(self, data):
        """add element to the end of list"""
        new_node = SingleNode(data)

        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """add element tot he start of list"""
        new_node = SingleNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, data, index):
        """insert element in desired position"""
        new_node = SingleNode(data)
        if index < 1:
            raise IndexError("Index out of bonds")
        elif index == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for i in range(1, index-1):
                if temp is not None:
                    temp = temp.next
            if temp is not None:
                new_node.next = temp.next
                temp.next = new_node
            else:
                print("The previous node is None")

    def insert_after_item(self, x, data):
        """insert element after specified node"""
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            raise Exception("Item not in list")
        else:
            new_node = SingleNode(data)
            new_node.next = n.next
            n.next = new_node

    def insert_before_item(self, x, data):
        """insert element before specified node"""
        if self.head is None:
            raise ValueError("No elements in list")
        if x == self.head.data:
            new_node = SingleNode(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Item is not in the list")
        else:
            new_node = SingleNode(data)
            new_node.next = n.next
            n.next = new_node

    def print_list(self):
        """prints linked list"""
        if self.head is None:
            print("List is empty")
        start = self.head
        while start is not None:
            print(f"->{start.data}")
            start = start.next

    def delete_by_value(self, key):
        """removes element by value from list"""
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def delete_by_index(self, index):
        """removes element by index from list"""
        if index < 0 or index >= self.get_size():
            raise IndexError('Index out of bounds')
        if index == 0:
            self.head = self.head.next
            return
        i = 0
        temp = self.head
        while temp is not None:
            if i == index-1:
                temp.next = temp.next.next
                break
            temp = temp.next
            i += 1

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

    def look_up(self, val):
        """finds index of desired element of list"""
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

    def is_empty(self):
        """:return true if list is empty"""
        return self.head is None


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    print(singly_linked_list.is_empty())
    singly_linked_list.append(69)
    singly_linked_list.append(2)
    singly_linked_list.prepend(20)
    singly_linked_list.append(122)
    singly_linked_list.print_list()
    print("\n")
    print(singly_linked_list.is_empty())
    singly_linked_list.insert_at_index(250, 3)
    singly_linked_list.delete_by_index(4)
    singly_linked_list.print_list()
