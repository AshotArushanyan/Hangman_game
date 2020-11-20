class Deque:
    def __init__(self):
        self.items = []

    def insert_front(self, data):
        return self.items.append(data)

    def insert_rear(self, data):
        return self.items.insert(0, data)

    def remove_front(self):
        if self.items:
            return self.items.pop()

    def remove_rear(self):
        if self.items:
            return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return self.items


def test_deque_functions(deque):

    print("\nTesting the functions of Deque:")

    # test insert_front and insert_rear

    for i in range(4):
        deque.insert_front(i)
    for i in range(1,4):
        deque.insert_rear(i)

    if deque.items == [3, 2, 1, 0, 1, 2, 3]:
        print("\nTest insert_front and insert_rear: PASS")
    else:
        print("\nTest insert_front and insert_rear: FAIL")

    # test remove_front and remove_rear

    for i in range(2):
        deque.remove_front()
    for i in range(2):
        deque.remove_rear()

    if deque.items == [1, 0, 1]:
        print("\nTest remove_front and remove_rear: PASS")
    else:
        print("\nTest remove_front and remove_rear: FAIL")

    # test is_empty

    for i in range(3):
        deque.remove_front()

    if deque:
        print("\nTest is_empty: FAIL")
    else:
        print("\nTest is_empty: PASS")


deque = Deque()
test_deque_functions(deque)