class HeapNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class MinHeap:

    def __init__(self):
        self.store = []

    def add(self, key, value=None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(logn)
            Space Complexity: O(1)
        """
        if value is None:
            value = key
        node = HeapNode(key, value)
        self.store.append(node)
        self.heap_up(len(self.store)-1)
        return None

    def remove(self):

        if self.empty():
            return None

        self.swap(0, len(self.store) - 1)
        pop = self.store.pop(len(self.store) - 1)
        self.heap_down(0)

        return pop.value

    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"

    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O(logn)
            Space complexity: O(1)
        """
        if len(self.store) == 0:
            return True

    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            This could be **very** helpful for the add method.
            Time complexity: O(logn)
            Space complexity: O(1)
        """
        # how can we do this recursively?
        parent_node_index = (index - 1)//2
        while self.store[index].key < self.store[parent_node_index].key and index > 0:
            self.swap(index, parent_node_index)
            index = parent_node_index
            parent_node_index = (index - 1)//2
        else:
            return self.store

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        left_child = (2*index) + 1
        right_child = (2*index) + 2

        if left_child < len(self.store):

            if right_child >= len(self.store):
                min_child = left_child
            elif self.store[left_child].key < self.store[right_child].key:
                min_child = left_child
            else:
                min_child = right_child

            if self.store[index].key > self.store[min_child].key:
                self.swap(index, min_child)
                self.heap_down(min_child)

    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
