"""Module contains Queue class based on doubly linked list"""

from doubly_linked_list import DoublyLinkedList


class Queue(DoublyLinkedList):
    """Queue representing class"""

    def enqueue(self, val):
        """Adds element in the end of a queue"""
        self.append(val)

    def dequeue(self):
        """Deletes element from the end of a queue"""
        self.pop_back()

    def peek(self):
        """Returns the last element of a queue"""
        return self.peek_back()

    def print_queue(self):
        """Prints queue"""
        self.print_list()


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(123)
    queue.enqueue("iuegr")
    queue.enqueue("uergh")
    queue.enqueue(4.5)
    print(queue.peek())
    queue.print_queue()
