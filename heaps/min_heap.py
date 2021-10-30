class HeapNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return self.__str__()


class MinHeap:

    def __init__(self):
        self.store = []

    def get_parent(self, node_index):

        return (node_index - 1) // 2

    def get_left_child(self, node_index):

        return (node_index * 2) + 1

    def get_right_child(self, node_index):
        return (node_index * 2) + 2

    def get_smallest_child(self, index):
        left = self.get_left_child(index)

        if left == len(self.store) - 1:
            return left
        else:
            right = self.get_right_child(index)

        if self.store[right].key < self.store[left].key:
            return right
        else:
            return left

    def add(self, key, value=None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: o(n log n)
            Space Complexity: o(1)
        """
        node = HeapNode(key, value)
        self.store.append(node)

        index = len(self.store) - 1

        self.heap_up(index)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: o(n log n)
            Space Complexity: o(1)
        """
        if self.empty():
            return None

        root = self.store[0]
        tail = len(self.store) - 1
        self.swap(0, tail)
        self.store.pop()
        if len(self.store) > 0:
            self.heap_down(0)
        return root.value

    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element.value) for element in self.store])}]"

    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: o(1)
            Space complexity: o(1)
        """
        return not self.store

    def heap_up(self, index):
        """ This helper method takes an index and
            moves it up the heap, if it is less than it's parent node.
            It could be **very** helpful for the add method.
            Time complexity: o(n log n )
            Space complexity: o(1)
        """
        while index != 0:
            node = self.store[index]
            parent_node = self.get_parent(index)

            if self.store[parent_node].key > node.key:
                self.swap(index, parent_node)
            index = parent_node

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves it down the heap if it is larger than it's children? 
            Time comlexity: o(n log n)
            Space complexity: 0(1)
        """
        node = self.store[index]

        while index < len(self.store) - 1:
            if (index * 2) + 1 >= len(self.store):
                return
            else:
                smallest_index = self.get_smallest_child(index)

            if node.key > self.store[smallest_index].key:
                self.swap(index, smallest_index)
                index = smallest_index
            else:
                return

    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
