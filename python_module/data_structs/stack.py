"""Module contains Stack class based on doubly linked list"""

from doubly_linked_list import DoublyLinkedList


class Stack(DoublyLinkedList):
    """Stack representing class"""

    def push(self, val):
        """Adds element at the end of stack"""
        self.append(val)

    def pop(self):
        """Deletes element from the end of a stack and returns it"""
        return self.pop_front()

    def peek(self):
        """:return last element of stack"""
        return self.peek_back()

    def print_stack(self):
        """prints stack"""
        self.print_list()


if __name__ == "__main__":
    stack = Stack()
    stack.push(8)
    stack.push(81)
    stack.push(34)
    stack.push(228)
    stack.print_stack()
    print("\n")
    print(stack.pop())
    print("\n")
    print(stack.peek())