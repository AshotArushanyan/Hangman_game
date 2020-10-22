# Problem 1
class CyclicDeque:
    def __init__(self):
        self.items = [None, None, None, None]
        self.size = 0

    def double_size(self):
        new_size = self.size * 2
        new_items = []
        for i in range(new_size):
            new_items.append(None)
        for i in range(self.size):
            new_items[i] = self.items[i]
        self.items = new_items

    def is_full(self):
        return self.size == len(self.items)

    def is_empty(self):
        return self.size == 0

    def add_first(self, data):
        if self.is_full():
            self.double_size()
        if self.items[0] is None:
            self.items[0] = data
        else:
            if self.items[-1] is None:
                self.items.pop()
                self.items.insert(0, data)
        self.size += 1

    def add_last(self, data):
        if self.is_full():
            self.double_size()
        self.items[self.size] = data
        self.size += 1

    def remove_first(self):
        self.items.pop(0)
        self.items.append(None)
        self.size -= 1

    def remove_last(self):
        self.items[self.size-1] = None
        self.size -= 1

    def get_first(self):
        return self.items[0]

    def get_last(self):
        return self.items[self.size-1]

    def __repr__(self):
        print(self.items)
        # I was getting an error about __str__ not returning string type, so I returned "" string to dodge the error!
        return ""

# -------------------------------------------------------


class Node:
    def __init__(self, data, next, previous):
        self.data = data
        self.next = next
        self.previous = previous


# Problem 3
class DoubleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def add_first(self, data):
        node = Node(data, self.first, None)
        if self.size == 0:
            self.first = node
            self.last = node
        else:
            if self.size == 1:
                self.last.previous = node
            self.first.previous = node
            self.first = node
        self.size += 1

    def add_last(self, data):
        node = Node(data, None, self.last)
        if self.size == 0:
            self.first = node
            self.last = node
        else:
            if self.size == 1:
                self.first.next = node
            self.last.next = node
            self.last = node
        self.size += 1

    def remove_first(self):
        if self.size == 0:
            print("The list was empty")
        else:
            if self.size == 1:
                self.first = None
                self.last = None
            else:
                self.first.next.previous = None
                temporary = self.first
                self.first = self.first.next
                temporary.next = None
                # self.first = self.first.next
            self.size -= 1

    def remove_last(self):
        if self.size == 0:
            print("The list was empty")
        else:
            if self.size == 1:
                self.first = None
                self.last = None
            else:
                self.last.previous.next = None
                self.last = self.last.previous
        self.size -= 1

    def insert_before(self, data, search_data):
        if self.size == 0:
            print("List is empty")
        else:
            current_node = self.first
            while current_node is not None:
                if current_node.data == search_data:
                    node = Node(data, current_node, current_node.previous)
                    if self.size == 1:
                        self.last.previous = node
                        self.first = node
                    elif current_node.previous is None:
                        self.first.previous = node
                        self.first = node
                    else:
                        current_node.previous.next = node
                        current_node.previous = node
                    self.size += 1
                    return
                else:
                    current_node = current_node.next
            print(f"{search_data} is not in the list!")
            return

    def insert_after(self, data, search_data):
        if self.size == 0:
            print("List is empty")
        else:
            current_node = self.first
            while current_node is not None:
                if current_node.data == search_data:
                    node = Node(data, current_node.next, current_node)
                    if self.size == 1:
                        self.first.next = node
                        self.last = node
                    elif current_node.next is None:
                        self.last.next = node
                        self.last = node
                    else:
                        current_node.next.previous = node
                        current_node.next = node
                    self.size += 1
                    return
                else:
                    current_node = current_node.next
            print(f"{search_data} is not in the list!")
            return

    def __repr__(self):
        current_node = self.get_first()
        print("None -> ", end="")
        while current_node is not None:
            print(f" <-({current_node.data})-> ", end="")
            current_node = current_node.next
        print(" <- None")
        # I was getting an error about __str__ not returning string type, so I returned "" string to dodge the error!
        return ""

# ----------------------------------------------------------------


# Problem 2
class LinkedListDeque:
    def __init__(self):
        self.items = DoubleLinkedList()

    def add_first(self, data):
        self.items.add_first(data)

    def add_last(self, data):
        self.items.add_last(data)

    def remove_first(self):
        self.items.remove_first()

    def remove_last(self):
        self.items.remove_last()

    def get_first(self):
        return self.items.first.data

    def get_last(self):
        return self.items.last.data

    def __repr__(self):
        current_node = self.items.get_first()
        deque = []
        while current_node is not None:
            deque.append(current_node.data)
            current_node = current_node.next
        print(deque)
        # I was getting an error about __str__ not returning string type, so I returned "" string to dodge the error!
        return ""


# Problem 4
def separating_evens_and_odds(linked_list):

    # I wrote you an email asking whether the two new lists have to be regular or linked.
    # Not to miss the deadline, I wrote both

    being_regular_python_lists = False

    if being_regular_python_lists:
        evens = []
        odds = []
        current_node = linked_list.first
        while current_node is not None:
            try:
                evens.append(current_node.data)
                odds.append(current_node.next.data)
                current_node = current_node.next.next
            except AttributeError:
                break
    else:
        evens = DoubleLinkedList()
        odds = DoubleLinkedList()
        current_node = linked_list.first
        while current_node is not None:
            try:
                evens.add_last(current_node.data)
                odds.add_last(current_node.next.data)
                current_node = current_node.next.next
            except AttributeError:
                break

    # I chose to print them and not to return because the command (return evens, odds) returns a tuple,
    # which makes the output look worse (adds (, ) in the end)
    # But if it is academically incorrect, I have the other way as well.

    better_looking_output = False

    if better_looking_output:
        print(f"{evens}")
        print(f"{odds}")
        return ""
    else:
        return evens, odds


# Problem 5
def main():

    # Testing CyclicDeque (Problem 1)

    print("------------------------------")
    print("Testing Cyclic Deque")
    print()

    cdq = CyclicDeque()

    # testing add_first and add_last

    cdq.add_first(5)
    cdq.add_first(9)
    cdq.add_last(2)
    cdq.add_last(4)
    cdq.add_first(0)

    if cdq.items == [0, 9, 5, 2, 4, None, None, None]:
        print("add_first and add_last test: PASS")
    else:
        print("add_first and add_last test: FAIL")

    # testing remove_first and remove_last

    cdq.remove_first()
    cdq.remove_last()
    cdq.remove_last()

    if cdq.items == [9, 5, None, None, None, None, None, None]:
        print("remove_first and remove_last test: PASS")
    else:
        print("remove_first and remove_last test: FAIL")

    # testing get_first and get_last

    if cdq.get_first() == 9:
        print("get_first test: PASS")
    else:
        print("get_first test: FAIL")

    if cdq.get_last() == 5:
        print("get_last test: PASS")
    else:
        print("get_last test: FAIL")

    # Testing LinkedListDeque (Problem 2)

    print("------------------------------")
    print("Testing Linked List Deque")
    print()

    lld = LinkedListDeque()

    # testing add_first and add_last

    lld.add_first(5)
    lld.add_first(9)
    lld.add_last(2)
    lld.add_last(4)
    lld.add_first(0)

    if lld.items.get_first().data == 0 and lld.items.get_last().data == 4:
        print("add_first and add_last test: PASS")
    else:
        print("add_first and add_last test: FAIL")

    # testing remove_first and remove_last

    lld.remove_first()
    lld.remove_last()
    lld.remove_last()

    if lld.items.get_first().data == 9 and lld.items.get_last().data == 5:
        print("remove_first and remove_last test: PASS")
    else:
        print("remove_first and remove_last test: FAIL")

    # testing get_first and get_last

    if lld.get_first() == 9:
        print("get_first test: PASS")
    else:
        print("get_first test: FAIL")

    if lld.get_last() == 5:
        print("get_last test: PASS")
    else:
        print("get_last test: FAIL")

    # Testing DoubleLinkedList (Problem 2)

    print("------------------------------")
    print("Testing Double Linked List")
    print()

    dll = DoubleLinkedList()

    # testing add_first and add_last

    dll.add_first(5)
    dll.add_first(9)
    dll.add_last(2)
    dll.add_last(4)
    dll.add_first(0)

    if dll.get_first().data == 0 and dll.get_last().data == 4:
        print("add_first and add_last test: PASS")
    else:
        print("add_first and add_last test: FAIL")

    # testing remove_first and remove_last

    dll.remove_first()
    dll.remove_last()
    dll.remove_last()

    if dll.get_first().data == 9 and dll.get_last().data == 5:
        print("remove_first and remove_last test: PASS")
    else:
        print("remove_first and remove_last test: FAIL")

    # testing get_first and get_last

    if dll.get_first().data == 9:
        print("get_first test: PASS")
    else:
        print("get_first test: FAIL")

    if dll.get_last().data == 5:
        print("get_last test: PASS")
    else:
        print("get_last test: FAIL")

    # Testing separating_evens_and_odds (Problem 4)

    print("------------------------------")
    print("Testing Separating evens and odds")
    print()

    dll_2 = DoubleLinkedList()

    for i in range(11):
        dll_2.add_last(i)

    evens, odds = separating_evens_and_odds(dll_2)
    current_node_evens = evens.first
    current_node_odds = odds.first
    all_evens = True
    all_odds = True

    for i in range(evens.size):
        if current_node_evens.data % 2 == 0:
            pass
        else:
            all_evens = False
        current_node_evens = current_node_evens.next

    for i in range(odds.size):
        if current_node_odds.data % 2 == 1:
            pass
        else:
            all_odds = False
        current_node_odds = current_node_odds.next

    if all_evens and all_odds:
        print("separating evens and odds test: PASS")
    else:
        print("separating evens and odds test: FAIL")

    print("------------------------------")


main()
