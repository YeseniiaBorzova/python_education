"""Module containing Hashtable class"""
from doubly_linked_list import DoublyLinkedList


class HashNode:
    """Class that stores pairs key, value in hashtable"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """Hashtable representing class"""
    def __init__(self):
        """Constructor"""
        self.list = DoublyLinkedList()
        for i in range(15):
            self.list.append(DoublyLinkedList())

    def hash(self, key):
        """:return hash of input key"""
        return key % 15

    def put(self, key, value):
        """puts element in the hash table"""
        hash_code = self.hash(key)
        node = HashNode(key, value)
        self.list.get_elem(hash_code).data.append(node)

    def get(self, key):
        """gets element by key from hashtable
        or -1 element doesnt not exists"""
        hash_code = self.hash(key)
        list = self.list.get_elem(hash_code).data
        cur = list.head
        while cur is not None:
            if cur.data.key == key:
                return cur.data.value
            cur = cur.next
        return -1

    def remove(self, key):
        """removes element by key from hashtable
        or -1 element doesnt not exists"""
        hash_code = self.hash(key)
        list = self.list.get_elem(hash_code).data
        cur = list.head
        while cur is not None:
            if cur.data.key == key:
                list.remove_by_value(cur.data)
                return
            cur = cur.next
        return -1


if __name__ == "__main__":
    hashTable = HashTable()
    hashTable.put(2, 27)
    hashTable.put(1, '234dwd')
    hashTable.put(29, 'arfhy')
    hashTable.put(3, '222bb')
    hashTable.put(16, 'uewyo')
    node = hashTable.get(16)
    print(node)
    hashTable.remove(2)
    node = hashTable.get(2)
    print(node)
