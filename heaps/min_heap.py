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


    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: ?
            Space Complexity: ?
        """
        if value == None:
            value = key
        self.store.append(HeapNode(key, value))
        self.heap_up(len(self.store) - 1)


    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: ?
            Space Complexity: ?
        """
        if self.empty():
            return None
        self.swap(0, len(self.store) - 1)
        removal = self.store.pop()
        self.heap_down(0)
        return removal.value


    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: ?
            Space complexity: ?
        """
        if not self.store:
            return True
        return False


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: ?
            Space complexity: ?
        """
        current_index = index
        parent_index  = (current_index - 1)//2
        while self.store[current_index].key < self.store[parent_index].key:
            self.swap (parent_index, current_index)
            current_index = parent_index
            if current_index == 0:
                break
            parent_index = (current_index - 1)//2


    def find_smallest(self, index1, index2):
        if index1 > len(self.store) - 1:
            return None
        elif index2 > len(self.store) - 1:
            smallest = index1
        elif self.store[index1].key < self.store[index2].key:
            smallest = index1
        else:
            smallest = index2
        return smallest

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """
        current_index = index
        left_child  = current_index * 2 + 1
        right_child = current_index * 2 + 2
        smallest = self.find_smallest(left_child, right_child)
        if not smallest:
            return None

        while self.store[current_index].key > self.store[smallest].key:
            self.swap(current_index, smallest)
            current_index = smallest
            left_child = current_index * 2 + 1
            right_child = current_index * 2 + 2
            smallest = self.find_smallest(left_child, right_child)
            if not smallest:
                return None


    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
