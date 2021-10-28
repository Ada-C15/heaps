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
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if value == None:
            value = key

        self.store.append(HeapNode(key, value))
        self.heap_up(len(self.store)-1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n)
            Space Complexity: O(1)
        """
        if self.empty():
            return None
        
        self.swap(0, len(self.store)-1)
        min_node = self.store.pop()
        self.heap_down(0)

        return str(min_node)

    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"

    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O(1)
            Space complexity: O(1)
        """
        return len(self.store) == 0

    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time complexity: O(log n)
            Space complexity: O(1)
        """
        parent_node = (index-1) // 2

        if index:
            if self.store[index].key < self.store[parent_node].key:
                self.swap(index, parent_node)
                self.heap_up(parent_node)


    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
        """

        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.store):

            if right_child >= len(self.store) or self.store[left_child].key < self.store[right_child].key:
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

