"""Module containing Hashtable class"""


class HashTable:
    """Class representing hashtable"""
    def __init__(self):
        """Constructor, by changing max attribute can be changed
        capacity of hash table"""
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        """generates hash code from key"""
        hash_code = 0
        for char in key:
            hash_code += ord(char)
        return hash_code % self.MAX

    def __getitem__(self, key):
        """magic method that allows to access to elements of table by key"""
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        """magic method that allows to set value to hashtable
        element by key"""
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        """deletes element from hash table by key"""
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                del self.arr[arr_index][index]


if __name__ == "__main__":
    hashtable = HashTable()
    hashtable['key1'] = 23
    hashtable['key2'] = 55
    hashtable['key3'] = 9
    hashtable['key4'] = 1111
    hashtable['key4'] = 27
    hashtable['key5'] = 'ertg'
    print(hashtable.arr)
    print(hashtable['key5'])
    del hashtable['key4']
    print(hashtable.arr)
