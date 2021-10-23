class HeapNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return self.value


class MinHeap:

    def __init__(self):
        self.store = []

    def find_parent(self, index):
        return (index - 1) // 2

    def find_left_child(self, index):
        return 2 * index + 1

    def find_right_child(self, index):
        return 2 * index + 2

    def add(self, key, value=None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if value is None:
            value = key

        node = HeapNode(key, value)
        self.store.append(node)
        self.heap_up(len(self.store) - 1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        # if heap does not contain any nodes return None
        if self.empty():
            return None

        # swap first element (smallest) with the last (larger) element
        self.swap(0, len(self.store) - 1)

        # pop smallest element out of the list
        min_node = self.store.pop()

        # heap down until it reaches proper level
        self.heap_down(0)

        return min_node.value

    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if self.empty():
            return "[]"
        return f"[{', '.join([str(node) for node in self.store])}]"

    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O(1)
            Space complexity: O(1)
        """
        if len(self.store) == 0:
            return True

    def heap_up(self, index):
        """ This helper method takes an index and
            moves it up the heap, if it is less than it's parent node.
            It could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(1)
        """
        i = index
        while i > 0:
            parent = self.find_parent(i)
            if self.store[i].key < self.store[parent].key:
                self.swap(i, parent)
                i = parent
            else:
                break

    def heap_down(self, index):
        """ This helper method takes an index and
            moves it down the heap if it's smaller
            than it's child node.
            Time complexity: O(log n)
            Space complexity: O(1)
        """

        i = index
        left = self.find_left_child(i)
        right = self.find_right_child(i)
        length = len(self.store)

        while i < length and left < length:

            if right < length:
                # both left and right children exist
                # swap with the smallest of them
                if self.store[left].key < self.store[right].key:
                    self.swap(i, left)
                    i = left
                else:
                    self.swap(i, right)
                    i = right
            else:
                # no right child
                # check if the only child is smaller:
                # yes -> swap
                # no -> break, because we reached the end of the heap
                if self.store[left].key < self.store[i].key:
                    self.swap(i, left)
                    i = left
                else:
                    break

            left = self.find_left_child(i)
            right = self.find_right_child(i)

    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        self.store[index_1], self.store[index_2] = self.store[index_2], self.store[index_1]
