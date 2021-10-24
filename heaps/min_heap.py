class HeapNode:

    # def initialize(self, key, value):
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
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        if value == None:
            value = key
        node = HeapNode(key, value)
        self.store.append(node)
        self.heap_up(len(self.store) - 1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(n)
            Space Complexity: O(n)
        """
        if len(self.store) == 0:
            return None
        self.swap(0, len(self.store) - 1)
        min = self.store.pop()
        self.heap_down(0)

        return min.value

    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"

    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: 0(1)
            Space complexity: 0(n)
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
        if index == 0:
                return index

        parent_node = (index - 1) // 2
        current_size = self.store
        if current_size[parent_node].key > current_size[index].key:
            self.swap(parent_node, index)
            self.heap_up(parent_node)

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves it up the heap if it's smaller
            than it's parent node.
        """
        
        current_size = self.store
        left_c = index * 2 + 1
        right_c= index * 2 + 2
        
        if left_c < len(self.store):
            if right_c < len(current_size):
                if current_size[left_c].key < current_size[right_c].key:
                    less = left_c
                else:
                    less = right_c
            else:
                less = left_c

            if current_size[index].key > current_size[less].key:
                self.swap(index, less)
                self.heap_down(less)

    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
