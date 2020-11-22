class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, data):
        return self.items.append(data)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return self.items


    
def test_queue_functions(queue):

    print("\nTesting the functions of Queue:")

    # test push
    for i in range(4):
        queue.enqueue(i)

    if queue.items == [0, 1, 2, 3]:
        print("\nTest enqueue: PASS")
    else:
        print("\nTest enqueue: FAIL")

    # test pop

    for i in range(2):
        queue.dequeue()

    if queue.items == [2, 3]:
        print("\nTest dequeue: PASS")
    else:
        print("\nTest dequeue: FAIL")

    # test is_empty

    for i in range(2):
        queue.dequeue()

    if queue:
        print("\nTest is_empty: FAIL")
    else:
        print("\nTest is_empty: PASS")


queue = Queue()
test_queue_functions(queue)
