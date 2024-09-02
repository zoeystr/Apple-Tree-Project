class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
   Raise Empty exception if the queue is empty.
   """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
   Raise Empty exception if the queue is empty.
   """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data  # keep track of existing list
        self._data = [None] * cap  # allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # front has been realigned


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self.data = []  # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self.data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self.data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self.data.append(e)  # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
   Raise Empty exception if the stack is empty.
   """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data[-1]  # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
   Raise Empty exception if the stack is empty.
   """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data.pop()  # remove last item from list


class AppleTree(ArrayQueue):
    def __init__(self):
        # create tree with 300 apples (this is a big tree!)
        super().__init__()
        self.tree = ArrayQueue()
        for x in range(0, 300, 1):
            self.tree.enqueue("apple")

    def display_contents(self):
        print("There are", tree.tree.__len__(), "apples in the tree")


class Basket:
    def __init__(self):
        self.basket = ArrayStack()

    def is_full(self):
        if self.basket.__len__() == 5:
            return True
        else:
            return False

    def display_contents(self):
        print("There are", basket.basket.__len__(), "apples in the basket")


class Wagon:
    def __init__(self):
        self.wagon = ArrayStack()

    def is_full(self):
        if self.wagon.__len__() == 40:
            return True
        else:
            return False

    def display_contents(self):
        print("There are", wagon.wagon.__len__(), "apples in the wagon")


class Storage:
    def __init__(self):
        self.storage = ArrayQueue()

    def display_contents(self):
        print("There are", storage.storage.__len__(), "apples in storage")


class Worker:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.inventory = []

    def pick_apple(self, group):  # used for picking from tree (queue)
        self.inventory.append(group.dequeue())
        print("apple picked")

    def store_apple(self, location):  # used for placing apples in storage (queue)
        location.enqueue(self.inventory[0])
        self.inventory.clear()
        print("apple stored")

    def place_apple(self, location):  # used for placing apples in baskets or wagons (stack)
        location.push(self.inventory[0])
        self.inventory.clear()
        print("apple placed")

    def take_apple(self, group):  # used for taking from basket and wagon (stack)
        self.inventory.append(group.pop())
        print("apple taken")


john = Worker('john', 25)
rachel = Worker('rachel', 26)

tree = AppleTree()
basket = Basket()
wagon = Wagon()
storage = Storage()

for time in range(1, 3600, 1):
    if (time % 10) == 0:
        if not tree.tree.is_empty():
            if basket.is_full():
                if wagon.is_full():
                    for fruit in range(0, 40, 1):
                        rachel.take_apple(wagon.wagon)
                        rachel.store_apple(storage.storage)
                    storage.display_contents()
                for fruit in range(0, 5, 1):
                    wagon.wagon.push(basket.basket.pop())
                wagon.display_contents()
            john.pick_apple(tree.tree)
            tree.display_contents()
            john.place_apple(basket.basket)
            basket.display_contents()

for fruit in range(0, 5, 1):
    wagon.wagon.push(basket.basket.pop())
for fruit in range(0, 20, 1):
    rachel.take_apple(wagon.wagon)
    rachel.store_apple(storage.storage)

tree.display_contents()
basket.display_contents()
wagon.display_contents()
storage.display_contents()
