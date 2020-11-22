class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        return self.items.append(data)

    def pop(self):
        if len(self.items) == 0:
            print("The stack is empty")
        else:
            return self.items.pop()

    def top(self):
        if self.items:
            return self.items[-1]

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return self.items


def test_stack_functions(stack):

    print("\nTesting the functions of Stack:")

    # test push
    for i in range(4):
        stack.push(i)

    if stack.items == [0, 1, 2, 3]:
        print("\nTest push: PASS")
    else:
        print("\nTest push: FAIL")

    # test pop

    for i in range(2):
        stack.pop()

    if stack.items == [0, 1]:
        print("\nTest pop: PASS")
    else:
        print("\nTest pop: FAIL")

    # test top

    top = stack.top()

    if top == 1:
        print("\nTest top: PASS")
    else:
        print("\nTest top: FAIL")

    # test is_empty

    for i in range(2):
        stack.pop()

    if stack:
        print("\nTest is_empty: FAIL")
    else:
        print("\nTest is_empty: PASS")


stack = Stack()
test_stack_functions(stack)
