class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:

    def __init__(self):
        self._capacity = 26
        self._hashtable = [None] * self._capacity * 10
        self._size = 0

    def _hash(self, element):
        return hash(element) % self._capacity
        # return ord(element[0]) % self._capacity

    def put(self, key, value):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if self._hashtable[i] is not None:
                if key == self._hashtable[i].key:
                    oldValue = self._hashtable[i].value
                    self._hashtable[i].value = value
                    return oldValue
            else:
                self._hashtable[index] = Entry(key, value)
                self._size += 1
                return None

    def get(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if self._hashtable[i] is not None:
                if key == self._hashtable[i].key:
                    return self._hashtable[i].value
            else:
                return None

    def hasKey(self, value):
        for element in self._hashtable:
            if element is not None:
                if element.value == value:
                    return element.key

    def remove(self, key):
        index = self._hash(key)
        while self._hashtable[index] is not None:
            if self._hashtable[index].key == key:
                break
            index = self._hash(index + 1)
        if self._hashtable[index] is None:
            return
        else:
            del self._hashtable[index]

    def size(self):
        return self._size

    def __iter__(self):
        for i in range(len(self._hashtable)):
            if self._hashtable[i] is not None:
                self._index = i
                break
        return self

    def __next__(self):
        if self._index >= len(self._hashtable):
            raise StopIteration
        tmpInd = self._index
        self._index = len(self._hashtable)
        for i in range(tmpInd + 1, len(self._hashtable)):
            if self._hashtable[i] is not None:
                self._index = i
                break

        return self._hashtable[tmpInd].value


def test_hashset_functions(hashmap):

    print("\nTesting the functions of Hashmap:")

    # test put

    hashmap.put(1, 12)
    hashmap.put(2, 22)
    hashmap.put(3, 5)
    hashmap.put(4, 10)
    hashmap.put(5, 3)

    list_to_test = []

    for i in hashmap:
        list_to_test.append(i)

    if list_to_test == [12, 22, 5, 10, 3]:
        print("\nTest put: PASS")
    else:
        print("\nTest put: FAIL")

    # test get

    if hashmap.get(2) == 22:
        print("\nTest get: PASS")
    else:
        print("\nTest get: FAIL")

    # test remove

    hashmap.remove(3)
    hashmap.remove(2)

    list_to_test = []

    for i in hashmap:
        list_to_test.append(i)

    if list_to_test == [12, 10, 3]:
        print("\nTest remove: PASS")
    else:
        print("\nTest remove: FAIL")

    # test haskey

    if hashmap.hasKey(12) == 1:
        print("\nTest haskey: PASS")
    else:
        print("\nTest haskey: FAIL")


hashmap = HashMap()
test_hashset_functions(hashmap)