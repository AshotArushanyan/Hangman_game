class Node:

    def __init__(self, data, next_level=None):
        self.data = data
        self.next = next_level

    def __repr__(self):
        string = ""
        node = self
        while node is not None:
            string += (str(node.data) + " -> ")
            node = node.next
        return string


class HashSet:

    def __init__(self, capacity):
        self._hashtable = [None] * capacity
        self._capacity = capacity
        self._size = 0

    def _hash(self, element):
        # print(hash(element))
        # print(hash(element) % self._capacity)
        return hash(element) % self._capacity

    def levelOrderIterator(self):
        for i in range(self._size):
            isYield = False
            for element in self._hashtable:
                for j in range(i):
                    if element is not None:
                        element = element.next
                if element is not None:
                    yield element.data
                    isYield = True
            if isYield is False:
                break

    def add(self, element):
        index = self._hash(element)
        if self._hashtable[index] is None:
            self._hashtable[index] = Node(element)
        else:
            n = Node(element, self._hashtable[index])
            self._hashtable[index] = n

    def contains(self, element):
        index = self._hash(element)
        n = self._hashtable[index]
        while n is not None:
            if n.data == element:
                return True
            n = n.next
        return False

    def remove(self, element):
        index = self._hash(element)
        n = self._hashtable[index]
        p = None
        while n is not None:
            if n.data == element:
                if p is None:
                    self._hashtable[index] = n.next
                else:
                    p.next = n.next
                n.next = None
                self._size -= 1
                return n
            p = n
            n = n.next
        return None

    def size(self):
        return self._size

    def intersection(self, s):
        newSet = HashSet(100)
        for element in self._hashtable:
            while element is not None:
                if s.contains(element.data):
                    newSet.add(element.data)
                element = element.next
        return newSet

    def __iter__(self):
        for element in self._hashtable:
            if element is not None:
                self._elem = element
                break
        return self

    def __next__(self):
        if self._elem is None:
            raise StopIteration
        tmp = self._elem
        if self._elem.next is not None:
            self._elem = self._elem.next
        else:
            index = self._hash(self._elem.data)
            self._elem = None
            for i in range(index + 1, len(self._hashtable)):
                if self._hashtable[i] is not None:
                    self._elem = self._hashtable[i]
                    break
        return tmp.data

    def __str__(self):
        return str(self._hashtable)


HS = HashSet(5)
HS.add(11)
HS.add(23)
HS.add(54)
HS.add(89)
HS.add(102)
HS.add(25)
HS.add(3)
HS.add(44)

print(HS)