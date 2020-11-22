class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"* {self.data} *"


class SingleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def get_size(self):
        return self.size

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def insert_first(self, data):
        node = Node(data, self.first)
        self.first = node
        if self.last is None:
            self.last = node
        self.size += 1

    def remove_first(self):
        if self.first is None:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first
        self.first = self.first.next
        tmp.next = None
        self.size -= 1

    def insert_last(self, data):
        node = Node(data, None)
        if self.last is None:
            self.first = node
            self.last = node
            self.size += 1
            return
        self.last.next = node
        self.last = node
        self.size += 1

    def remove_last(self):
        if self.size == 0:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first
        # Iterate over the linked list to get a reference of the pre-last element
        while tmp.next != self.last:
            tmp = tmp.next
        tmp.next = None
        self.last = tmp
        self.size -= 1

    def insert_before(self, new_data, old_data):
        if self.size == 0:
            print("List is empty")
        else:
            current_node = self.first
            previous_node = None
            while current_node is not None:
                if current_node.data == old_data:
                    node = Node(new_data, current_node)
                    if previous_node is None:
                        self.first = node
                    else:
                        previous_node.next = node
                    self.size += 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next
            print("There is no such data in the list")

    def insert_after(self, new_data, old_data):
        if self.size == 0:
            print("List is empty")
        else:
            current_node = self.first
            while current_node is not None:
                if current_node.data == old_data:
                    node = Node(new_data, current_node.next)
                    if current_node.next is None:
                        current_node.next = node
                        self.last = node
                    else:
                        current_node.next = node
                    self.size += 1
                    return
                else:
                    current_node = current_node.next
            print("There is no such data in the list")

    def find(self, data):
        current_node = self.first
        while current_node is not None:
            if current_node.data == data:
                return data
            else:
                current_node = current_node.next

    def remove(self, data):
        current_node = self.first
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.first = current_node.next
                self.size -= 1
                return
            else:
                previous_node = current_node
                current_node = current_node.next

    def index_of(self, data):
        current_node = self.first
        index = 0
        while current_node is not None:
            if current_node.data == data:
                return index
            else:
                current_node = current_node.next
                index += 1

    def print_list(self):
        current_node = self.first
        while current_node is not None:
            print(f"{current_node}")
            current_node = current_node.next


def test_list_functions(list):

    print("\nTesting the functions of single linked list:")

    # test insert_first and insert_last

    list.insert_first(1)
    list.insert_first("a")
    list.insert_last("b")
    list.insert_last("c")
    list.insert_first(4)

    if list.first.data == 4 and list.last.data == "c":
        print("\nInsert First/Last Test: PASS")
    else:
        print("\nInsert First/Last Test:FAIL")

    # test remove_first and remove_last

    list.remove_first()
    list.remove_last()
    list.remove_last()

    if list.first.data == "a" and list.last.data == 1:
        print("\nRemove First/Last Test:PASS")
    else:
        print("\nRemove First/Last Test:FAIL")

    # test first, last, and size

    if list.size == list.get_size():
        print("\nGet list size: PASS")
    else:
        print("\nGet list size: FAIL")

    if list.first == list.get_first():
        print("\nGet first element: PASS")
    else:
        print("\nGet first size: FAIL")

    if list.last == list.get_last():
        print("\nGet last element: PASS")
    else:
        print("\nGet last size: FAIL")

    # test insert_after and insert_before

    list.insert_after(2,1)
    list.insert_before("b","a")

    previous_node = None
    current_node = list.first
    new_list = []
    while current_node is not None:
        new_list.append(current_node.data)
        current_node = current_node.next
    if new_list == ["a","b",1,2]:
        print("\nInsert Before/After Test: PASS")
    else:
        print("\nInsert Before/After Test: PASS")

    # test remove

    list.remove("b")
    list.remove(1)

    current_node = list.first
    new_list = []
    while current_node is not None:
        new_list.append(current_node.data)
        current_node = current_node.next
    if new_list == ["a",2]:
        print("\nRemove Test: PASS")
    else:
        print("\nRemove Test: FAIL")

    # test index_of

    if list.index_of("a") == 0:
        print("\nIndex of element Test: PASS")
    else:
        print("\nIndex of element Test: FAIL")


sll = SingleLinkedList()
# test_list_functions(sll)







